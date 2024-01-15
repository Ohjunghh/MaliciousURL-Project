from ipwhois import IPWhois
import socket
import pandas as pd
from urllib.parse import urlparse

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except (socket.gaierror, socket.error, socket.herror, socket.timeout) as e:
        print(f"Error getting IP address for {domain}: {e}")
        return None

def get_whois_info(domain):
    ip_address = get_ip_address(domain)
    
    if ip_address is not None:
        ipwhois = IPWhois(ip_address)
        try:
            result = ipwhois.lookup_rdap()  # RDAP로 조회
            return result
        except Exception as e:
            print(f"Error looking up RDAP for {ip_address}: {e}")
    return None

def get_netname(url):
    parts = urlparse(url)
    domain = parts.hostname
    whois_info = get_whois_info(domain)
    
    if whois_info is not None:
        nets_info = whois_info.get('network', {})
        name = nets_info.get('name', '')
        if name:
            return name
        else:
            print(f"No nets information for {domain}")
    else:
        print(f"Unable to retrieve WHOIS information for {domain}")
    return None
    
def get_feature_netname(dataframe):
    try:
        dataframe['netname'] = dataframe['url'].apply(get_netname)
    except Exception as e:
        print(f"Error processing URLs: {e}")
"""
csv_file_path = 'C:/URL/normal_dataset/success/example3000.csv' #'C:/URL/normal_dataset/success/example10.csv' 
df = pd.read_csv(csv_file_path, header=None, names=['url'])
get_feature_netname(df)
df.to_csv('C:/URL/normal_dataset/netname/example3000_netname.csv', index=False)
"""