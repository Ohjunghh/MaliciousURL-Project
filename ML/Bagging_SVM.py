import pandas as pd
import warnings
from sklearn.svm import SVC
from sklearn.ensemble import BaggingClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
import joblib

warnings.filterwarnings('ignore')

path = 'C:/MaliciousURL-Project/result/real/'
datasets = pd.read_csv(path + 'MLtest.csv',header=0)

# 데이터프레임에서 열을 추출하여 새로운 데이터프레임 생성
x = datasets.iloc[:, 1:35]
y = datasets[['abnormal']]

# 훈련 데이터와 테스트 데이터로 분할
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Bagging에 사용할 SVM 모델 설정
svm_model = SVC(kernel='linear')

# Bagging 알고리즘 적용
clf = BaggingClassifier(estimator=svm_model, 
                                  n_estimators=10, 
                                  max_samples=1.0, 
                                  bootstrap=False, 
                                  n_jobs=1, 
                                  random_state=42)
clf.fit(X_train, y_train)

# 예측
pred = clf.predict(X_test)

# 평가
accuracy = accuracy_score(y_test, pred)
recall = recall_score(y_test, pred)
precision = precision_score(y_test, pred)
f1 = f1_score(y_test, pred)

# 결과 출력
print("Accuracy:", accuracy)
print("Recall:", recall)
print("Precision:", precision)
print("F1-Score:", f1)


joblib.dump(clf,'C:/MaliciousURL-Project/result/real/bagging.pkl')