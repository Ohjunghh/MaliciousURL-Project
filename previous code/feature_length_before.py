import pandas as pd
import numpy as np
from urllib.parse import urlparse
import csv
import tldextract

df=pd.read_csv('C:/URL/abnormal/openphish_0110-0111.csv', header=None)
abnormal_url=df.values #pandas DataFrame을 사용하여 CSV 데이터를 NumPy 배열로 읽기
                     #values()함수를 사용하여이를numpy()배열로 변환
abnormal_url_list=df.values[:,-1]

domain_len=[] #domain 길이
path_len=[]# Path 길이
parameter_len=[]# Parameter 길이
tld_len=[]# TLD 길이

for url in abnormal_url_list:
    parts = urlparse(url)
    tldparts=tldextract.extract(url)
    domain_len.append(len(parts.hostname))
    path_len.append(len(parts.path))
    parameter_len.append(len(parts.query))
    tld_len.append(len(tldparts.suffix))
   
feature_len=pd.DataFrame()
feature_len['len_domain']=domain_len
feature_len['len_path']=path_len
feature_len['len_parameter']=parameter_len
feature_len['len_tld']=tld_len

feature_len.to_csv('C:/URL/abnormal/openphish_0110-0111_feature_len.csv')



