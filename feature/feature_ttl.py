import dns.resolver
from urllib.parse import urlparse
import pandas as pd

def get_dns_ttl(url):
    try:
        host = urlparse(url).hostname

        result = dns.resolver.resolve(host, 'A')

        ttl = result.rrset.ttl

        return ttl

    except Exception as e:
        return f"Error: {e}"
    
def get_feature_ttl(dataframe):
    dataframe['ttl'] = dataframe['url'].apply(get_dns_ttl)
