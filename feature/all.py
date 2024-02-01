import pandas as pd
import whois
from urllib.parse import urlparse
from whois.parser import PywhoisError
from datetime import datetime
import re
import tldextract
from ipwhois import IPWhois
import socket
import dns.resolver
from ipwhois.exceptions import IPDefinedError

def check_extension(url):
    # 특정 단축사이트와 일치하는 정규 표현식
    extension_pattern = (
        r'.*\.(bit\.ly|kl\.am|cli\.gs|bc\.vc|po\.st|v\.gd|bkite\.com|shorl\.com|scrnch\.me|to\.ly|adf\.ly|x\.co|1url\.com|ad\.vu|migre\.me|su\.pr|3\.ly|'
        r'smallurl\.co|cutt\.us|filoops\.info|shor7\.com|yfrog\.com|tinyurl\.com|u\.to|ow\.ly|ff\.im|rubyurl\.com|r2me\.com|post\.ly|twitthis\.com|vvd\.im|'
        r'buzurl\.com|cur\.lv|tr\.im|bl\.lnk|tiny\.cc|lnkd\.in|q\.gs|is\.gd|hurl\.ws|om\.ly|prettylinkpro\.com|qr\.net|qr\.ae|snipurl\.com|ity\.im|t\.co|'
        r'db\.tt|link\.zip\.net|doiop\.com|url4\.eu|poprl\.com|tweez\.me|short\.ie|me2\.do|bit\.do|shorte\.st|go2l\.ink|yourls\.org|wp\.me|goo\.gl|j\.mp|'
        r'twurl\.nl|snipr\.com|shortto\.com|vzturl\.com|u\.bb|shorturl\.at|han\.gl|wo\.gl|wa\.gl|url\.kr|me2\.kr|zrr\.kr|buly\.kr|lrl\.kr|vo\.la|han\.gl|shrunken\.com)$'
    )

    # URL이 패턴과 일치하는지 확인
    match = re.search(extension_pattern, url)
    # 일치하면 1을, 그렇지 않으면 0을 반환
    return 1 if match else 0

def get_feature_url_shortening(dataframe):
    # 해당 열에 대해 check_extension 함수를 적용하여 결과를 새로운 열에 저장
    dataframe['url_shortening'] = dataframe['url'].apply(check_extension)

def get_dns_ttl(url):
    try:
        host = urlparse(url).hostname

        result = dns.resolver.resolve(host, 'A')

        ttl = result.rrset.ttl

        return ttl

    except Exception as e:
        return f"Error: {e}"
    
def get_feature_ttl(dataframe):
    dataframe['ttl'] = dataframe['url'].apply(get_dns_ttl)

#ip 가져오기
def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except (socket.gaierror, socket.error, socket.herror, socket.timeout) as e:
        print(f"Error getting IP address for {domain}: {e}")
        return None
    
def get_ipwhois_info(domain):
    ip_address = get_ip_address(domain)
    
    if ip_address is not None:
        try:
            ipwhois = IPWhois(ip_address)
            try:
                result = ipwhois.lookup_rdap()  # RDAP로 조회
                return result
            except Exception as e:
                print(f"Error looking up RDAP for {ip_address}: {e}")
        except IPDefinedError as e:
            # IPDefinedError가 발생하면 사설 IP 주소이므로 에러 메시지 출력
            print(f"Private-Use IP address {ip_address}: {e}")
    return None

#normal_netnames_df = pd.read_csv('path/to/normal_netnames.csv') #나중에 추가해야함...!
#NORMAL_NETNAMES = normal_netnames_df['netname'].tolist()
#netname 가져오기

def get_netname(url):
    parts = urlparse(url)
    domain = parts.hostname
    
    if domain is not None:
        whois_info = get_ipwhois_info(domain)
        if whois_info is not None:
            nets_info = whois_info.get('network', {})
            name = nets_info.get('name', '')
            print(name)
            if name:
                return name
            else:
                print(f"No nets information for {domain}")
        else:
            print(f"Unable to retrieve WHOIS information for {domain}")
    else:
        print("Invalid URL without a hostname")
        
    return None

def get_feature_netname(dataframe):
    try:
        dataframe['netname'] = dataframe['url'].apply(get_netname)
    except Exception as e:
        print(f"Error processing URLs: {e}")

def calculate_lengths(url):
    try:
        if url is None:
            return 0, 0, 0, 0  # URL이 None인 경우에 대한 예외 처리

        parts = urlparse(url)
        tldparts = tldextract.extract(url)
        
        # 도메인, Path, Parameter, TLD 길이
        len_domain = len(parts.hostname) if parts.hostname else 0
        len_path = len(parts.path) if parts.path else 0
        len_parameter = len(parts.query) if parts.query else 0
        len_tld = len(tldparts.suffix) if tldparts.suffix else 0

        return len_domain, len_path, len_parameter, len_tld

    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None, None, None

def get_feature_length(dataframe):
    # 각 URL에 대해 길이 계산
    lengths = dataframe['url'].apply(calculate_lengths).tolist()
    # 계산된 길이를 DataFrame에 추가
    dataframe[['len_domain', 'len_path', 'len_parameter', 'len_tld']] = pd.DataFrame(lengths, index=dataframe.index)


def check_https_protocol(url):
    protocol = urlparse(url).scheme
    return "1" if protocol == "https" else "0"

def get_feature_https(dataframe):
    dataframe['https'] = dataframe['url'].apply(check_https_protocol)

def check_extension(url):
    # 정규 표현식을 사용하여 주어진 확장자들과 일치하는지 확인
    match = re.search(r'.*\.(php|html|htm|jpg|dll|hwp|hwpx|pptx|docx|iso|js|lnk|vbs|xls|xml|zip|xlsx|txt|exe|bin|i|sh|asp|xlsb|vi|pdf|gif|bot|sys|aspx|png|py|jar|tar|rar|arm|arc|bat|spc|sparc|wav|vbs|vbe|wsf|wsc|hta|ppc|m)$', url)
    # 일치하면 extension을 1로, 그렇지 않으면 0으로 반환
    return 1 if match else 0

def get_feature_file_extension(dataframe):
    # 해당 열에 대해 check_extension 함수를 적용하여 결과를 새로운 열에 저장
    dataframe["file_extension"] = dataframe['url'].apply(check_extension)


def get_feature_count(dataframe):
    # 각 URL에 대해 결과 계산 및 DataFrame에 열 추가
    for i, url in enumerate(dataframe['url']):
        result = count_special_characters(url)
        for char, count in result.items():
            dataframe.at[i, f'\'{char}\''] = count

def count_special_characters(url):
    special_characters = {'%': 0, '$': 0, '=': 0, '@': 0, '?': 0, '&': 0, '#': 0, '.': 0, '_': 0, '-': 0, ';': 0, '{': 0, '}': 0, '[': 0, ']': 0, '|': 0, '+': 0, '*': 0}
    for char in url:
        if char in special_characters:
            special_characters[char] += 1
    return special_characters

def calculate_uppercase_ratio(url):
    total_chars = len(url)
    uppercase_chars = sum(1 for char in url if char.isupper())

    if total_chars == 0:
        return 0.0

    uppercase_ratio = round(uppercase_chars / total_chars,5)
    return uppercase_ratio

#전체숫자비율
def calculate_digit_ratio(url):
    total_chars = len(url)
    digit_chars = sum(1 for char in url if char.isdigit())

    if total_chars == 0:
        return 0.0

    digit_ratio = round(digit_chars / total_chars,5)
    return digit_ratio

#호스트 모음/자음 비율
def calculate_consonant_vowel_ratio(url):
    parsed_url = urlparse(url)
    host = parsed_url.netloc

    vowels = set("aeiouAEIOU")
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")

    vowel_count = sum(1 for char in host if char in vowels)
    consonant_count = sum(1 for char in host if char in consonants)

    total_chars = vowel_count + consonant_count

    if total_chars == 0:
        return 0.0

    consonant_vowel_ratio = round(consonant_count / total_chars,5)
    return consonant_vowel_ratio


def get_whois_info(domain):
    try:
        info = whois.whois(domain)
        return info
    except PywhoisError as e:
        print(f"Error retrieving WHOIS information for {domain}: {e}")
        return None

def get_day(url):
    parts = urlparse(url)
    domain = parts.hostname

    try:
        if domain is not None:
            whois_info = get_whois_info(domain)
            if whois_info is not None:
                creation = whois_info.get('creation_date')
                update = whois_info.get('updated_date')
                expiration = whois_info.get('expiration_date')
                
                if creation or update or expiration:
                    creation = creation[0] if isinstance(creation, list) else creation
                    update = update[0] if isinstance(update, list) else update
                    expiration = expiration[0] if isinstance(expiration, list) else expiration
                    
                    nowdate = datetime(2024, 1, 23)
                    
                    Creation_day = (nowdate - creation).days if creation else None
                    Update_day = (nowdate - update).days if update else None
                    Expiration_day = (expiration - nowdate).days if expiration else None
                    Expiration_Creation_day = (expiration - creation).days if expiration and creation else None

                    return Creation_day, Update_day, Expiration_day, Expiration_Creation_day

    except Exception as e:
        print(f"Error processing URL {url}: {e} \n")

    return None, None, None, None

def get_feature_day(dataframe):
    try:
        # get_day 함수를 적용하여 새로운 열 생성
        dataframe[['Creation_day', 'Update_day', 'Expiration_day', 'Expiration_Creation_day']] = dataframe['url'].apply(get_day).apply(pd.Series)
    except (Exception, pd.errors.EmptyDataError, pd.errors.ParserError) as e:
        print(f"Error processing URLs: {e}")

def get_feature_uppercase_ratio(dataframe):
    dataframe['uppercase'] = dataframe['url'].apply(calculate_uppercase_ratio)

def get_feature_digit_ratio(dataframe):
    dataframe['digit_ratio'] = dataframe['url'].apply(calculate_digit_ratio)

def get_feature_consonant_vowel(dataframe):
    dataframe['consonant_vowel'] = dataframe['url'].apply(calculate_consonant_vowel_ratio)

#main
print(datetime.now())
csv_file_path ="C:/MaliciousURL-Project/kaggle_abnormal.csv"

try:
    df = pd.read_csv(csv_file_path, header=None,names=['url'],skiprows=120000,nrows=2)
    print(df+"\n")
except pd.errors.EmptyDataError:
    print(f"File at path {csv_file_path} is empty.")
  
get_feature_netname(df)  # netname
get_feature_day(df)  # now-create, now-update, end-now, end-create
get_feature_ttl(df)  # ttl
get_feature_length(df)  # len_domain, len_path, len_parameter, len_tld
get_feature_count(df)  # count_special
get_feature_uppercase_ratio(df)
get_feature_digit_ratio(df)
get_feature_consonant_vowel(df)
get_feature_https(df)  # https
get_feature_file_extension(df)  # file_extension
get_feature_url_shortening(df)  # url_shortening

df.to_csv('C:/MaliciousURL-Project/result/test.csv', index=False)
print(datetime.now())
