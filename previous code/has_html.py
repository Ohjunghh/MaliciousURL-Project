import re
import pandas as pd

def check_extension(url):
    # 정규 표현식을 사용하여 주어진 확장자들과 일치하는지 확인
    match = re.search(r'.*\.(php|html|htm|jpg|dll|hwp|hwpx|pptx|docx|iso|js|lnk|vbs|xls|xml|zip|xlsx|txt|exe|bin|i|sh|asp|xlsb|vi|pdf|gif|bot|sys|aspx|png|py|jar|tar|rar|arm|arc|bat|spc|sparc|wav|vbs|vbe|wsf|wsc|hta|ppc|m)$', url)

    # 일치하면 extension을 1로, 그렇지 않으면 0으로 반환
    return 1 if match else 0

def process_excel(input_excel_path, output_excel_path):
    # 엑셀 파일로부터 URL을 읽어오기
    df = pd.read_excel(input_excel_path, header=None, names=["URL"])

    # 해당 열에 대해 check_extension 함수를 적용하여 결과를 새로운 열에 저장
    df["Extension Check"] = df["URL"].apply(check_extension)

    # 결과를 새로운 엑셀 파일로 저장
    df.to_excel(output_excel_path, index=False)

# 예시 사용:
input_excel_path = "input_urls.xlsx"
output_excel_path = "output_results_php_html_.xlsx"
process_excel(input_excel_path, output_excel_path)
