import re
import os
import pandas as pd

def check_extension(url):
    # 특정 확장자와 일치하는 정규 표현식
    extension_pattern = (
        r'.*\.(bit\.ly|kl\.am|cli\.gs|bc\.vc|po\.st|v\.gd|bkite\.com|shorl\.com|scrnch\.me|to\.ly|adf\.ly|x\.co|1url\.com|ad\.vu|migre\.me|su\.pr|'
        r'smallurl\.co|cutt\.us|filoops\.info|shor7\.com|yfrog\.com|tinyurl\.com|u\.to|ow\.ly|ff\.im|rubyurl\.com|r2me\.com|post\.ly|twitthis\.com|'
        r'buzurl\.com|cur\.lv|tr\.im|bl\.lnk|tiny\.cc|lnkd\.in|q\.gs|is\.gd|hurl\.ws|om\.ly|prettylinkpro\.com|qr\.net|qr\.ae|snipurl\.com|ity\.im|t\.co|'
        r'db\.tt|link\.zip\.net|doiop\.com|url4\.eu|poprl\.com|tweez\.me|short\.ie|me2\.do|bit\.do|shorte\.st|go2l\.ink|yourls\.org|wp\.me|goo\.gl|j\.mp|'
        r'twurl\.nl|snipr\.com|shortto\.com|vzturl\.com|u\.bb|shorturl\.at|han\.gl|wo\.gl|wa\.gl)$'
    )

    # URL이 패턴과 일치하는지 확인
    match = re.search(extension_pattern, url)

    # 일치하면 1을, 그렇지 않으면 0을 반환
    return 1 if match else 0

def process_excel(input_excel_path, output_excel_path):
    # 입력 파일이 존재하는지 확인
    if not os.path.exists(input_excel_path):
        print(f"오류: 입력 파일 '{input_excel_path}'을 찾을 수 없습니다.")
        return

    # 엑셀 파일로부터 URL을 읽어오기
    df = pd.read_excel(input_excel_path, header=None, names=["URL"])

    # 해당 열에 대해 check_extension 함수를 적용하여 결과를 새로운 열에 저장
    df["Extension Check"] = df["URL"].apply(check_extension)

    # 결과를 새로운 엑셀 파일로 저장
    df.to_excel(output_excel_path, index=False)

# 예시 사용:
input_excel_path = "input_urls.xlsx"
output_excel_path = "output_results_short.xlsx"
process_excel(input_excel_path, output_excel_path)
