import os
from lightgbm import LGBMClassifier
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
import joblib

#열 이름에서 특수문자 없애야함..... LightGBMError: Do not support special JSON characters in feature name.
# 경고 무시 설정
import warnings
warnings.filterwarnings('ignore')

project_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(project_dir, 'ML/urldataset.csv')
model_output_path = os.path.join(project_dir, 'ML/result/LightGBM.pkl')

# CSV 데이터 읽기
datasets = pd.read_csv(data_path)

# 데이터프레임에서 열을 추출하여 새로운 데이터프레임 생성
x = datasets.iloc[:, 1:34]
y = datasets[['abnormal']]


# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# model training
lgbm_wrapper = LGBMClassifier(n_estimators=200,max_depth=5,num_leaves=20,learning_rate=0.1,random_state=42)

#callbacks=[lgb.early_stopping(stopping_rounds=50)
#pip install lightgbm==3.3.2

evals = [(X_test, y_test)] 
lgbm_wrapper.fit(X_train, y_train, eval_metric='logloss', eval_set=evals)

# predict 
y_pred = lgbm_wrapper.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Recall:", recall)
print("Precision:", precision)
print("F1-Score:", f1)

joblib.dump(lgbm_wrapper,model_output_path)
"""
Accuracy: 0.9885277777777778
Recall: 0.9841914834400223
Precision: 0.992756878158338
F1-Score: 0.9884556254367576
"""