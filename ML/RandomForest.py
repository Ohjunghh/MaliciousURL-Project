import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import warnings
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
import joblib

warnings.filterwarnings('ignore')

path = './ML/'
datasets = pd.read_csv(path + 'urldataset2.csv')


# 데이터프레임에서 열을 추출하여 새로운 데이터프레임 생성
x = datasets.iloc[:, 1:34]
y = datasets[['abnormal']]


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


clf = RandomForestClassifier(n_estimators=100,
    max_depth=16,
    min_samples_split=3,
    min_samples_leaf=1,
    max_features='sqrt',
    random_state=42)
clf.fit(X_train, y_train)

pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, pred)
recall = recall_score(y_test, pred)
precision = precision_score(y_test, pred)
f1 = f1_score(y_test, pred)

print("Accuracy:", accuracy)
print("Recall:", recall)
print("Precision:", precision)
print("F1-Score:", f1)

joblib.dump(clf,'./ML/real_result/RandomForest.pkl')

"""
Accuracy: 0.9888888888888889
Recall: 0.9846924575563596
Precision: 0.9929834409205726
F1-Score: 0.9888205701509223
"""