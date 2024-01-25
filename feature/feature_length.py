import pandas as pd
from urllib.parse import urlparse
import tldextract

def calculate_lengths(url):
    parts = urlparse(url)
    tldparts = tldextract.extract(url)
    # 도메인, Path, Parameter, TLD 길이
    return len(parts.hostname), len(parts.path), len(parts.query), len(tldparts.suffix)

def get_feature_length(dataframe):
    # 각 URL에 대해 길이 계산
    lengths = dataframe['url'].apply(calculate_lengths).tolist()
    # 계산된 길이를 DataFrame에 추가
    dataframe[['len_domain', 'len_path', 'len_parameter', 'len_tld']] = pd.DataFrame(lengths, index=dataframe.index)
