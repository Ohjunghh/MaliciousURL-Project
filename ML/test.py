import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
import joblib
import warnings

warnings.filterwarnings('ignore')

# 현재 스크립트 경로 기준으로 동적 경로 설정
project_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(project_dir, 'ML/urldataset2.csv')

# CSV 데이터 읽기
datasets = pd.read_csv(data_path)

# 데이터프레임에서 열을 추출하여 새로운 데이터프레임 생성
x = datasets.iloc[:, 1:34]
y = datasets[['abnormal']]
 
#print(x.info())

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


# 모델 파일 경로 동적으로 설정
model_path = os.path.join(project_dir, 'ML/real_result/Logisitic.pkl')

# 모델 불러오기
clf = joblib.load(model_path)

y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Recall:", recall)
print("Precision:", precision)
print("F1-Score:", f1)