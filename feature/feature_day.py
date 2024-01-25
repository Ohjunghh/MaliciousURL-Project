import whois
import pandas as pd
from urllib.parse import urlparse
from whois.parser import PywhoisError
from datetime import datetime

    
# whois 정보 가져오기
def get_whois_info(domain):
    try:
        info = whois.whois(domain)
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
                    
                    
                    nowdate = datetime(2024,1,23)
<<<<<<< HEAD
                    # timedelta 객체를 사용하여 날짜 차이 계산
                    """
                    Creation_day = (nowdate - creation).days if isinstance(creation, datetime) else (nowdate - creation[0]).days
                    Update_day = (nowdate - update).days if isinstance(update, datetime) else (nowdate - update[0]).days
                    Expiration_day = (expiration - nowdate).days if isinstance(expiration, datetime) else (expiration[0] - nowdate).days
                    Expiration_Creation_day = (expiration - creation).days if isinstance(expiration, datetime) and isinstance(creation, datetime) else (
                        expiration[0] - creation[0]).days
                    """

                    Creation_day = (nowdate - creation).days #f isinstance(creation, datetime) else (nowdate - creation).days
                    Update_day = (nowdate - update).days #f isinstance(update, datetime) else (nowdate - update).days
                    Expiration_day = (expiration - nowdate).days #f isinstance(expiration, datetime) else (expiration - nowdate).days
                    Expiration_Creation_day = (expiration - creation).days #f isinstance(expiration, datetime) and isinstance(creation, datetime) else (
                            #xpiration - creation).days
                    print("creation : "+str(creation)+"\n"+"update:"+str(update)+"\n"+"expiration:"+str(expiration)+"\n")
                    print("Creation_day:"+str(Creation_day))   
                    print("Update_day:" + str(Update_day))
                    print("Expiration_day:" + str(Expiration_day))
                    print("\n")   
=======
                    
                    Creation_day = (nowdate - creation).days 
                    Update_day = (nowdate - update).days 
                    Expiration_day = (expiration - nowdate).days 
                    Expiration_Creation_day = (expiration - creation).days 
>>>>>>> 1784c5ba7b43460946a285a6240c3efea2514dd3
                    
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
        

<<<<<<< HEAD
<<<<<<< HEAD
#예시 사용법 C:\URL\abnormal_dataset\download
=======
# 예시 사용법 C:\URL\abnormal_dataset\download
>>>>>>> 52854ee76eb8c7a0581f840bf16226eb35d7d33f
#csv_file_path = 'C:/URL/abnormal_dataset/download/URLhaus+openphish_url_0111.csv'#'C:/URL/abnormal_dataset/download/URLhaus+openphish_url_0111.csv' 
#df = (pd.read_csv(csv_file_path, header=None, names=['url'])).head(5)        
#get_feature_day(df)
#print(df)
#df.to_csv('C:/URL/abnormal_dataset/URLhaus+openphish_url_0111_day', index=False)
=======
>>>>>>> 1784c5ba7b43460946a285a6240c3efea2514dd3
