import dns.resolver
from urllib.parse import urlparse

def get_dns_ttl(url):
    try:
        host = urlparse(url).hostname

        result = dns.resolver.resolve(host, 'A')

        ttl = result.rrset.ttl

        return ttl

    except Exception as e:
        print(f"Error : {e}")
        return None
    
#Version: 2.5.0
from scapy.all import * 
from urllib.parse import urlparse

def get_icmp_ttl(url):
  
    parts = urlparse(url)
    domain = parts.hostname
   
    try:
        # Send an ICMP Echo Request and receive a response
        response = sr1(IP(dst=domain)/ICMP(), timeout=2, verbose=False)

        # Extract TTL value from the response
        if response:
            return response.ttl
        else:
            return None
    except Exception as e:
        print(f"Error occurred while getting TTL for {domain}: {e}")
        return None

def get_combined_ttl(url):
    dns_ttl = get_dns_ttl(url)
    
    if dns_ttl is not None:
        return dns_ttl
    else:
        return get_icmp_ttl(url)

def get_feature_ttl(dataframe):
    dataframe['ttl'] = dataframe['url'].apply(get_combined_ttl)