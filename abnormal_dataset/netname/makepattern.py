import pandas as pd

csv_file_path = 'C:/MaliciousURL-Project/result/finalnetname.csv' 
df = pd.read_csv(csv_file_path, header=None, names=['netname'])
string=''

for netname in df['netname'][:-1]:
    string+=(netname+"|")

string+=str(df['netname'].tail(1).iloc[0])

# 파일 경로 및 이름
file_path = "C:/MaliciousURL-Project/result/abnormal_netname.txt"  # 실제 경로와 원하는 파일 이름으로 변경

# 파일 열기 (쓰기 모드로)
with open(file_path, "w", encoding="utf-8") as file:  # 자동으로 파일이 닫힘
    # 문자열 파일에 쓰기
    file.write(string)

print(f"문자열이 {file_path}에 저장되었습니다.")

