import whois
import pandas as pd
from urllib.parse import urlparse
from whois.parser import PywhoisError
from datetime import datetime

    
# whois 정보 가져오기
def get_whois_info(domain):
    try:
        info = whois.whois(domain)
        print(info)
        return info
    except PywhoisError as e:
        print(f"Error retrieving WHOIS information for {domain}: {e}")
        return None
    
def get_day(url):
    parts = urlparse(url)
    domain = parts.hostname

    try:
        if domain is not None:
            whois_info = get_whois_info(domain)
            if whois_info is not None:
                if 'creation_date' in whois_info and 'updated_date' in whois_info and 'expiration_date' in whois_info:
                    
                    creation = whois_info['creation_date']
                    update = whois_info['updated_date']
                    expiration = whois_info['expiration_date']
                    
                    creation = creation[0] if isinstance(creation, list) else creation
                    update = update[0] if isinstance(update, list) else update
                    expiration = expiration[0] if isinstance(expiration, list) else expiration
                    
                    
                    nowdate = datetime.now()#datetime(2024,1,23)
                    
                    Creation_day = (nowdate - creation).days 
                    Update_day = (nowdate - update).days 
                    Expiration_day = (expiration - nowdate).days 
                    Expiration_Creation_day = (expiration - creation).days 

                    
                    return Creation_day, Update_day, Expiration_day, Expiration_Creation_day
                   
    except Exception as e:
        print(f"Error processing URL {url}: {e} \n")

    return None, None, None, None


def get_feature_day(dataframe):
    try:
        # get_day 함수를 적용하여 새로운 열 생성
        dataframe[['Creation_day', 'Update_day', 'Expiration_day', 'Expiration_Creation_day']] = dataframe['url'].apply(get_day).apply(pd.Series)
    except (Exception, pd.errors.EmptyDataError, pd.errors.ParserError) as e:
        print(f"Error processing URLs: {e}")
