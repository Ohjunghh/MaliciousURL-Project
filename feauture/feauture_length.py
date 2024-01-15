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

"""
# CSV 파일 경로
csv_file_path = 'C:/URL/abnormal/openphish_0110-0111.csv' 

# CSV 파일을 읽어와 'url'이라는 열로 이름을 설정한 DataFrame 생성
df = pd.read_csv(csv_file_path, header=None, names=['url'])

# feature_length 함수를 사용하여 길이기반특징 계산
get_feature_length(df)

# 결과를 CSV 파일로 저장
# 인덱스 포함 x . 포함하면 맨 앞 열에 숫자열생김
df.to_csv('C:/URL/abnormal/rrrr.csv', index=False)
"""