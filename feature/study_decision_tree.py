import pandas as pd
import matplotlib.pyplot as plt   # plot 패키지
from sklearn.datasets import load_iris() # 데이터 불러오기
from sklearn.tree import DecisionTreeClassifier as DT, plot_tree # decision tree
plt.rcParams['axes.unicode_minus'] = False       # 마이너스 부호 깨짐 현상 
plt.rcParams["font.family"] = 'NanumBarunGothic' # 한글폰트 전역 설정

data = load_iris() # 데이터 넣어주기
X_train, X_test, Y_train, Y_test = train_test_split(data.data, data.target, random_state=0) #학습 데이터, 평가 데이터 분할해주기

clf0 = DT(max_depth=3, random_state=0) # 의사결정트리 초기화 해주기
clf0.fit(X_train, Y_train) # 학습시키기 (특징값, 정답값)

# 트리 모형 시각화
plt.figure(figsize=(5,4), dpi=200)
plot_tree(clf0, 
         feature_names = data.feature_names,
         #["꽃받침길이", "꽃받침폭",  "꽃잎길이", "꽃잎폭" ], 
         class_names=data.target_names,
         filled=True) #클래스별로 색칠
plt.show()

from sklearn.tree import export_text
r = export_text(clf0, feature_names=iris['feature_names'])
print(r)