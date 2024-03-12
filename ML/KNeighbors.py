from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import warnings
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
import joblib

warnings.filterwarnings('ignore')

path = 'C:/MaliciousURL-Project/ML/'
datasets = pd.read_csv(path + 'urldataset.csv')


# 데이터프레임에서 열을 추출하여 새로운 데이터프레임 생성
x = datasets.iloc[:, 1:34]
y = datasets[['abnormal']]

# 훈련 데이터와 테스트 데이터로 분할
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)



# Bagging 알고리즘 적용
clf  = KNeighborsClassifier(n_neighbors=5,
                            weights='distance', #디폴트는 uniform
                            )
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


joblib.dump(clf,'C:/MaliciousURL-Project/ML/result/KNN.pkl')
