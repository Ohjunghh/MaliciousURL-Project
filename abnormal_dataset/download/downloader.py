from requests import get  
from datetime import datetime 
import os
import csv

def download(url, file_name):
    try:
        now = datetime.now()
        now=now.strftime('%m%d')
        file_name = file_name + now + '.csv' #날짜 시간 붙이기
        file_path = 'C:/MaliciousURL-Project/abnormal_dataset/download'#저장할 경로
        full_path = os.path.join(file_path, file_name)

        with open(full_path, "a+", newline='', encoding='utf-8') as csv_file:   
            response = get(url)               
            content = response.text
            csv_writer = csv.writer(csv_file)
           
            for line in content.split('\n'):
                csv_writer.writerow([line])
        print(f"Download and save as CSV successful. File saved as: {full_path}")
    except Exception as e:
        print(f"Error during download: {e}")      

if __name__ == '__main__':
	url = "https://openphish.com/feed.txt"
	download(url,"openphish_")
       
#출처 https://blog.naver.com/shino1025/221279112390