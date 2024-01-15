import pandas as pd

def count_special_characters(url):
    special_characters = {'%': 0, '$': 0, '=': 0, '@': 0, '?': 0, '&': 0, '#': 0, '.': 0, '_': 0, '-': 0, ';': 0, '{': 0, '}': 0, '[': 0, ']': 0, '|': 0, '+': 0, '*': 0}

    for char in url:
        if char in special_characters:
            special_characters[char] += 1

    return special_characters

# CSV 파일 경로
csv_file_path = 'C:/Users/seyeo/OneDrive/바탕 화면/졸프/openphish_0110.csv'  # 경로만 바꿔서하면 됨
# CSV 파일 읽기
df = pd.read_csv(csv_file_path)

# URL 데이터 가져오기
url_column_name = df.columns[0]  # 첫 번째 열을 URL로 가정
url_data = df[url_column_name].values

# 각 URL에 대해 결과 계산 및 출력
for url in url_data:
    result = count_special_characters(url)
    
    print(f"URL: {url}")
    print("특수 문자 개수:")
    for char, count in result.items():
        print(f"{char}: {count}")
    print("\n")

# 결과를 데이터프레임으로 변환
result_df = pd.DataFrame(list(map(count_special_characters, url_data)))

# 결과를 엑셀 파일로 저장
result_df.to_excel('output_result.xlsx', index=False)