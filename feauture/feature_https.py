from urllib.parse import urlparse
import pandas as pd

def check_https_protocol(url):
    protocol = urlparse(url).scheme
    return "1" if protocol == "https" else "0"

def get_feature_https(dataframe):
    dataframe['https'] = dataframe['url'].apply(check_https_protocol)
"""
csv_file_path = 'C:/URL/abnormal/openphish_0110-0111.csv' 
df = pd.read_csv(csv_file_path, header=None, names=['url'])
get_feature_https(df)
df.to_csv('C:/URL/abnormal/httpshas.csv', index=False)
"""