import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import warnings
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

warnings.filterwarnings('ignore')

path = 'C:/MaliciousURL-Project/result/real/'
datasets = pd.read_csv(path + 'MLtest.csv',header=0)


# 데이터프레임에서 열을 추출하여 새로운 데이터프레임 생성
x = datasets.iloc[:, 1:35]
y = datasets[['abnormal']]


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


clf = HistGradientBoostingClassifier(
    learning_rate=0.1,  
    max_iter=100,       
    max_bins=255,       
    random_state=42
)
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

joblib.dump(clf,'C:/MaliciousURL-Project/result/real/hist.pkl')