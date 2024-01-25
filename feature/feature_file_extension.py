import re
import pandas as pd

def check_extension(url):
    # 정규 표현식을 사용하여 주어진 확장자들과 일치하는지 확인
    match = re.search(r'.*\.(php|html|htm|jpg|dll|hwp|hwpx|pptx|docx|iso|js|lnk|vbs|xls|xml|zip|xlsx|txt|exe|bin|i|sh|asp|xlsb|vi|pdf|gif|bot|sys|aspx|png|py|jar|tar|rar|arm|arc|bat|spc|sparc|wav|vbs|vbe|wsf|wsc|hta|ppc|m)$', url)
    # 일치하면 extension을 1로, 그렇지 않으면 0으로 반환
    return 1 if match else 0

def get_feature_file_extension(dataframe):
    # 해당 열에 대해 check_extension 함수를 적용하여 결과를 새로운 열에 저장
    dataframe["file_extension"] = dataframe['url'].apply(check_extension)

