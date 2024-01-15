from urllib.parse import urlparse
import pandas as pd

def check_https_protocol(url):
    protocol = urlparse(url).scheme
    return "1" if protocol == "https" else "0"

def process_excel(input_excel_path, output_excel_path):
    df = pd.read_excel(input_excel_path, header=None, names=["URL"])
    df["HTTPS Protocol"] = df["URL"].apply(check_https_protocol) #이거 그대로 사용하면 됨
    df.to_excel(output_excel_path, index=False)

input_excel_path = "input_urls.xlsx"
output_excel_path = "output_results_https.xlsx"
process_excel(input_excel_path, output_excel_path)





