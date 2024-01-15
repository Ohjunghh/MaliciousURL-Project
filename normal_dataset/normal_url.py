#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd #앞으로 pd라는 이름으로 pandas를 사용
import ssl, socket
import csv
from datetime import datetime

# 소켓 연결 제한 시간 설정
socket.setdefaulttimeout(2)

#현재 시간을 반환해주는 함수
def cur_time() :
    time = datetime.now()
    time_s = "[%s:%s:%s]"  % (time.hour, time.minute, time.second)
    return time_s

# HTTPS 연결 요청 함수
def https_connect(url) :
    ctx = ssl.create_default_context() # SSL 연결을 위한 기본 설정의 SSLContext 객체를 받음
    s = ctx.wrap_socket(socket.socket(), server_hostname=url) #소켓 객체(socket.socket())와 연결할 URL(server_hostname=url)을 받아 SSLSocket 객체를 받음
    s.connect((url, 443)) #  소켓 연결을 수행하고 해당 소켓을 반환 #SSL의 포트 번호는 TCP/443번
    return s

print(cur_time(), "Program start..!")

df=pd.read_csv('C:/URL/normal/top-1m.csv', header=None, usecols=[1])
normal_url=df.values #pandas DataFrame을 사용하여 CSV 데이터를 NumPy 배열로 읽기
                     #values()함수를 사용하여이를numpy()배열로 변환

scheme_s = "https://"
convert_url = []
failed_url = []
failed_url_err = []
suc_count = 0
failed_count = 0

src = 35500
dst = 38000
urllist = normal_url[src:dst,-1]

for url in urllist:
    try :
        https_connect(url)
        url = scheme_s + url
        convert_url.append(url)
        suc_count += 1
        print(url, "-> conversion succeed!!")
    except Exception as e:
        failed_url.append(url)
        failed_url_err.append(e)
        failed_count += 1
        print(url, "-> conversion failed..")
        pass


print(cur_time(), "Convert complete..!")

# 변환 성공한 URL들을 CSV 파일 형식으로 저장    
f = open("C:/URL/normal/https-top-1m_4-1.csv", 'a', encoding="UTF-8", newline="")
csv_wr = csv.writer(f)
for i in range(len(convert_url)) :
    csv_wr.writerow( [convert_url[i]])    
f.close()
 
# 변환에 실패한 URL들을 CSV 파일 형식으로 저장
f = open("C:/URL/normal/failed-top-1m_4-1.csv", 'a', encoding="euc_kr", newline="")
csv_wr = csv.writer(f)
for i in range(len(failed_url)) :
    csv_wr.writerow( [failed_url[i], failed_url_err[i]])
f.close()


# In[ ]:





# In[ ]:




