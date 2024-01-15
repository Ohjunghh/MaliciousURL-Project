import re
import pandas as pd

def get_numeric_ratio(url):
    # 정규 표현식을 사용하여 URL에서 숫자를 찾음
    numbers = re.findall(r'\d', url)
    
    # URL 내 숫자의 개수
    num_count = len(numbers)
    
    # 전체 URL의 길이
    total_length = len(url)
    
    # 전체 숫자 비율
    numeric_ratio = round((num_count / total_length) * 100, 2)
    
    return numeric_ratio

def get_feature_count_number(dataframe):
    # 각 URL에 대해 get_numeric_ratio 함수 호출
    dataframe['numeric ratio'] = dataframe['url'].apply(get_numeric_ratio)
"""
csv_file_path = 'C:/URL/abnormal_dataset/URLhaus+openphish_url_0111.csv' 
df = pd.read_csv(csv_file_path, header=None, names=['url'])
get_feature_count_number(df) 
df.to_csv('C:/URL/abnormal_dataset/after_data processing/URLhaus+openphish_url_0111_numeric_ratio.csv', index=False)
"""