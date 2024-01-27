import pandas as pd
from urllib.parse import urlparse
import tldextract

def calculate_lengths(url):
    parts = urlparse(url)
    tldparts = tldextract.extract(url)
    # 도메인, Path, Parameter, TLD 길이
    len_domain = len(parts.hostname) if parts.hostname else 0
    len_path = len(parts.path) if parts.path else 0
    len_parameter = len(parts.query) if parts.query else 0
    len_tld = len(tldparts.suffix) if tldparts.suffix else 0
    
    return len_domain, len_path, len_parameter, len_tld


def get_feature_length(dataframe):
    # None 값이 포함된 행 제거
    dataframe = dataframe.dropna(subset=['url'])
    
    # 각 URL에 대해 길이 계산
    lengths = dataframe['url'].apply(calculate_lengths).tolist()
    
    # 계산된 길이를 DataFrame에 추가
    dataframe[['len_domain', 'len_path', 'len_parameter', 'len_tld']] = pd.DataFrame(lengths, index=dataframe.index)