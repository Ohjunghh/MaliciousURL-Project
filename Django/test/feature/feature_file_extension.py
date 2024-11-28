import re
from urllib.parse import urlparse
import pandas as pd
def check_file_extension(url):
    try:
        parsed_url = urlparse(url)
        path = parsed_url.path
        if not path:
            return 0
        # 정규 표현식을 사용하여 주어진 확장자들과 일치하는지 확인.*\.
        match = re.search(r'\.([^\/]+)($|/|php|php1|php2|php3|php4|php5|php7|php8|phtml|phps|html|htm|chm|shtml|jpg|jpeg|dll|hwp|hwpx|ppt|pptx|docx|doc|iso|js|jse|jsp|lnk|vbs|xls|xlsm|xla|xlam|xml|zip|xlsx|txt|psd|exe|inf|uue|bin|i|sh|asp|sln|xlsb|vi|pdf|gif|bot|gsf|scr|sys|com|aspx|cgi|au3|ps|eps|ps1|ahk|tmp|log|png|py|lsp|jar|tar|rar|rev|arm|ini|reg|arc|gz|7z|tgz|xz|bat|rtf|spc|sparc|wav|mp3|mp4|m4v|mpg|mpeg|api|wmv|mwa|asf|avi|webm|vbs|vbe|wsf|wsh|wsc|hta|ppc|m|ame|sh4|68k|m68k|m68|xxe|xe|a|so|dmp|lib|cmd|fas|r00|r01|r02|r03|r04|r05|r06|r07|r08|r09|msi|file|x86|xxe|pif|img|apk|url|z|one|arj|pl|inc|iva|vhd|pm4|vkm|dat)', path, re.IGNORECASE)
        # 일치하면 extension을 1로, 그렇지 않으면 0으로 반환
        return 1 if match else 0
    except Exception as e:
        print(f"Error processing URL {url}: {e} \n")
    return None

def get_feature_file_extension(dataframe):
    # 해당 열에 대해 check_extension 함수를 적용하여 결과를 새로운 열에 저장
    dataframe["file_extension"] = dataframe['url'].apply(check_file_extension)


csv_file_path ="C:/MaliciousURL-Project/result/part/test.csv"#"C:/MaliciousURL-Project/kaggle_abnormal.csv"
df = pd.read_csv(csv_file_path, header=None,names=['url'])
  
get_feature_file_extension(df)  # file_extension
df.to_csv('C:/MaliciousURL-Project/result/test-fileextension.csv', index=False)

