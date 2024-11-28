from urllib.parse import urlparse
import pandas as pd

def check_https_protocol(url):
    protocol = urlparse(url).scheme
    return "1" if protocol == "https" else "0"

def get_feature_https(dataframe):
    dataframe['https'] = dataframe['url'].apply(check_https_protocol)
