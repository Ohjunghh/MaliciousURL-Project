# import requests
# import certifi
# html가져오기???????????????

# # HTTPS 요청 보내기
# response = requests.get('https://www.naver.com', verify=certifi.where())

# # 응답 내용 출력
# print(response.text)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
 
'''
For each URL and each port listed in the given configuration file, access the URL via HTTPS and retrieve the server's certificate.
Alert in Slack if the certificate is invalid or expiring soon.
 
'''
 
__author__ = "Videre Research, LLC"
__version__ = "1.0.2"
 
 
# I M P O R T S ###############################################################
 
import datetime
import os
import sys
import socket
import ssl
import logging
import requests
import json
from threading import Thread
import certifi
from urllib.parse import urlparse

if (sys.version_info > (3, 0)):
    from urllib.parse import urljoin
else:
    from urlparse import urljoin
 
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
 
 
# G L O B A L S ###############################################################
 
 
number_of_days = 60
 
webhookURL = None
slack_base_url = 'https://hooks.slack.com/services/'
environment_variable_name = 'slack_api'
 
slack_user = 'SSL Certificate Validation'
slack_message_title = 'SSL Certificate Check'
slack_icon = ':shield:'
 
hasErrors = False
 
filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ssl.yaml")
 
logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.info("-" * 80)
logger.info("Version:  %s" % (__version__))
logger.info("Path:    %s" % (os.path.realpath(__file__)))
 
context = ssl.create_default_context()
context.options = ssl.CERT_REQUIRED
context.verify_flags &= ssl.VERIFY_CRL_CHECK_LEAF
context.verify_flags &= ssl.VERIFY_CRL_CHECK_CHAIN
context.check_hostname = True
context.load_verify_locations(cafile=certifi.where())
 
 
# C O D E #####################################################################
 
 
def time_this(original_function):
    def new_function(*args, **kwargs):
        before = datetime.datetime.now()
        x = original_function(*args, **kwargs)
        after = datetime.datetime.now()
        global logger
        logger.info('Duration: %.4fs  %s' % ((after - before).total_seconds(), original_function))
        return x
    return new_function
 
 
def requests_retry_session(
    retries=3,
    backoff_factor=2.5,
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session
 
 
def get_environment_variable(myVariable):
    """Sets value based on a required environment variable."""
    if os.getenv(myVariable, '') == "":
        logger.error('Environment variable ' + myVariable + ' not set, exiting')
        sys.exit(1)
    if os.getenv(myVariable, '') == "Y":
        return True
    elif os.getenv(myVariable, '') == "N":
        return False
    else:
        return os.getenv(myVariable, '')
 
 
@time_this
def sendSlack(severity, body):
    """Send a given message to Slack."""
    global webhookURL
    if severity == 'Healthy':
        color = '36a64f'
        alert = ''
    elif severity == 'Minor':
        color = 'FFD700'
        alert = ''
    elif severity == 'Major':
        color = 'FF8C00'
        alert = '<!channel|channel> '
    elif severity == 'Critical':
        color = 'FF4500'
        alert = '<!channel|channel> '
    else:
        color = '2F4F4F'
        alert = ''
 
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    data = {
        "username": slack_user,
        "icon_emoji": slack_icon,
        "text": alert + slack_message_title,
        "attachments": [
            {
                "fallback": body,
                "color": color,
                "text": body
            }
        ]
    }

    # logger.info("Sending message to Slack")
    # try:
    #     r = requests_retry_session().request(method='POST', url=urljoin(slack_base_url, webhookURL), data=json.dumps(data), headers=headers, timeout=25)
    # except Exception as x:
    #     logger.error('Connection failed :( %s' % x.__class__.__name__)
    # else:
    #     if r.status_code == 200:
    #         response = r.content
    #         logger.info(response)
    #     else:
    #         logger.error('Error: %s' % r.status_code)
    #         logger.debug(r.headers)
    #         logger.debug(r.text)
    #         logger.debug(sys.exc_info()[:2])
    # finally:
    #     logger.info('Sent to Slack')
 
 
def get_issuer(ssl_info):
    try:
        commonname = ""
        orgname = ""
        domain = []
        for entry in ssl_info['issuer']:
            if entry[0][0] == 'organizationName':
                orgname = entry[0][1]
            if entry[0][0] == 'commonName':
                commonname = entry[0][1]
            if entry[0][0] == 'domainComponent':
                domain.append(entry[0][1])
 
        return f'{commonname}, {orgname}'  # , {".".join(domain)}'
    except:
        return str(ssl_info['issuer'])
 
 
def check_certificate(hostname, port):
    ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'
    global hasErrors
    global context
    conn = context.wrap_socket(
        socket.socket(socket.AF_INET),
        server_hostname=hostname,
    )
    conn.settimeout(10.0)
 
    slack_body = f"SSL Certificate: https://{hostname}:{port}\n"
    try:
        conn.connect((hostname, port))
        ssl_info = conn.getpeercert()
 
        # parse the string from the certificate into a Python datetime object
        logger.info(f"TLS Version: {conn.version()}")
        logger.info(f"TLS Cipher: {conn.cipher()[0]}")
        logger.info(f"Certificate Issuer: {get_issuer(ssl_info)}")
        expires = datetime.datetime.strptime(ssl_info['notAfter'], ssl_date_fmt)
        logger.info(f"SSL cert for {hostname} expires on {expires.isoformat()}")
        remaining = expires - datetime.datetime.utcnow()
        logger.info(remaining)
        if remaining < datetime.timedelta(days=0):
            logger.info(f"Cert expired {remaining.days} days ago")
            slack_body += f"Cert expired {remaining.days} days ago"
            sendSlack('Critical', slack_body)
            hasErrors = True
        elif remaining < datetime.timedelta(days=number_of_days):
            logger.info(f"Cert expiring in {remaining.days} days")
            slack_body += f"Cert expiring in {remaining.days} days"
            sendSlack('Minor', slack_body)
            hasErrors = True
        else:
            logger.info("Cert OK")
    except Exception as e:
        logger.error("Error {0}".format(str(e)))
        slack_body += "Error {0}".format(str(e))
        sendSlack('Major', slack_body)
        hasErrors = True
    finally:
        conn.close()
        logger.info('-'*30)
 
def main():
    """Main function."""
    global webhookURL

    # URL 입력
    url = input("Enter the URL to check SSL certificate: ")

    # URL을 사용하여 호스트와 포트 추출
    parsed_url = urlparse(url)
    server = parsed_url.hostname
    port = parsed_url.port if parsed_url.port else 443  # 기본 포트는 443입니다.

    # SSL 인증서 확인
    logger.info(f'Checking certificate on server {server} port {port}')
    check_certificate(server, port)

    if not hasErrors:
        sendSlack('Healthy', 'The SSL certificate is OK')

    logger.info('*** DONE ***')
    sys.exit(0) 

# def main():
#     """Main function."""
#     global webhookURL
 
#     webhookURL = get_environment_variable(environment_variable_name)
 
#     if os.path.isfile(filepath):
#         try:
#             result = yaml.load(open(filepath), yaml.SafeLoader)
#         except Exception as e:
#             logger.error('YAML Error: %s' % e)
#             sys.exit(1)
#     else:
#         logger.error('File not found: %s' % filepath)
#         sys.exit(1)
 
#     logger.info(result)
#     for server, ports in result.items():
#         for port in ports:
#             logger.info('Checking certificate on server %s port %s' % (server, port))
#             worker = Thread(target=check_certificate(server, port, ))
#             worker.setDaemon(True)
#             worker.start()
 
#     worker.join()
 
#     if not hasErrors:
#         sendSlack('Healthy', 'All certificates checked are OK')
 
#     logger.info('*** DONE ***')
#     sys.exit(0)
 
###############################################################################
 
 
if __name__ == "__main__":
    main()
 
# E N D   O F   F I L E #######################################################
#URL의 SSL 인증서를 확인하기 위해 해당 서버와 포트(기본값인 443 포트)로 연결합니다.
#연결이 성공하면 TLS 버전, 암호화 알고리즘, 인증서 발급자 및 만료 날짜
# 인증서의 만료까지 남은 기간을 표시 
#만약 인증서가 만료되었거나, 만료까지 일정 기간 내에 있는 경우에는 이를 Slack으로 알립니다.
#인증서가 유효할 때 "Cert OK" 메시지가 표시됩니다.