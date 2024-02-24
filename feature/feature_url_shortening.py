import re
import pandas as pd
from urllib.parse import urlparse

def check_url_shortening(url):
    domain = urlparse(url).netloc
    # 특정 확장자와 일치하는 정규 표현식
    extension_pattern = (
        r'(bit\.ly|kl\.am|cli\.gs|bc\.vc|po\.st|v\.gd|bkite\.com|shorl\.com|scrnch\.me|to\.ly|adf\.ly|x\.co|1url\.com|ad\.vu|migre\.me|su\.pr|3\.ly|rb\.gy|eurl\.kr|'
        r'smallurl\.co|cutt\.us|filoops\.info|shor7\.com|yfrog\.com|tinyurl\.com|u\.to|ow\.ly|ff\.im|rubyurl\.com|r2me\.com|post\.ly|twitthis\.com|vvd\.im|vvd\.bz|'
        r'buzurl\.com|cur\.lv|tr\.im|bl\.lnk|tiny\.cc|lnkd\.in|q\.gs|is\.gd|hurl\.ws|om\.ly|prettylinkpro\.com|qr\.net|qr\.ae|snipurl\.com|ity\.im|t\.co|'
        r'db\.tt|link\.zip\.net|doiop\.com|url4\.eu|poprl\.com|tweez\.me|short\.ie|short\.io|bit\.do|shorte\.st|go2l\.ink|yourls\.org|wp\.me|goo\.gl|j\.mp|'
        r'twurl\.nl|snipr\.com|shortto\.com|vzturl\.com|u\.bb|shorturl\.at|han\.gl|wo\.gl|wa\.gl|url\.kr|me2\.kr|zrr\.kr|buly\.kr|lrl\.kr|vo\.la|han\.gl|shrunken\.com)$'
    )

    # URL이 패턴과 일치하는지 확인
    match = re.match(extension_pattern, domain)
    # 일치하면 1을, 그렇지 않으면 0을 반환
    return 1 if match else 0

def get_feature_url_shortening(dataframe):
    # 해당 열에 대해 check_extension 함수를 적용하여 결과를 새로운 열에 저장
    dataframe['url_shortening'] = dataframe['url'].apply(check_url_shortening)

