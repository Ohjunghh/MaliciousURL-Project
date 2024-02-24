import pandas as pd 
csv_file_path='C:/MaliciousURL-Project/result/kaggle-abnormal_all_realreal.csv'

import chardet
try:
    with open(csv_file_path, 'rb') as f:
        result = chardet.detect(f.read())
except FileNotFoundError:
    print(f"File not found at path: {csv_file_path}")
    exit()

encoding = result['encoding']
try:
    data=pd.read_csv(csv_file_path,encoding=encoding)
except pd.errors.EmptyDataError:
    print(f"File at path {csv_file_path} is empty.")
  
shuffled_data=data.sample(frac=1,random_state=42)
shuffled_data.to_csv("C:/MaliciousURL-Project/result/kaggle-abnormal_all_realreal_mix",index=False)