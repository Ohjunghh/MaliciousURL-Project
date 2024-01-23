import pandas as pd

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
"""
# CSV 파일 경로
csv_file_path = 'C:/URL/abnormal/openphish_0110-0111.csv'  # 경로만 바꿔서하면 됨
# CSV 파일 읽기
df = pd.read_csv(csv_file_path,header=None, names=['url']) 
#함수사용
get_feature_count(df)
# 결과를 csv 파일로 저장
df.to_csv('C:/URL/abnormal/real5_end.csv', index=False)
"""