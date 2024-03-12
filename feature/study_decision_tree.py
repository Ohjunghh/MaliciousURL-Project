import pandas as pd
import matplotlib.pyplot as plt   # plot ��Ű��
from sklearn.datasets import load_iris() # ������ �ҷ�����
from sklearn.tree import DecisionTreeClassifier as DT, plot_tree # decision tree
plt.rcParams['axes.unicode_minus'] = False       # ���̳ʽ� ��ȣ ���� ���� 
plt.rcParams["font.family"] = 'NanumBarunGothic' # �ѱ���Ʈ ���� ����

data = load_iris() # ������ �־��ֱ�
X_train, X_test, Y_train, Y_test = train_test_split(data.data, data.target, random_state=0) #�н� ������, �� ������ �������ֱ�

clf0 = DT(max_depth=3, random_state=0) # �ǻ����Ʈ�� �ʱ�ȭ ���ֱ�
clf0.fit(X_train, Y_train) # �н���Ű�� (Ư¡��, ���䰪)

# Ʈ�� ���� �ð�ȭ
plt.figure(figsize=(5,4), dpi=200)
plot_tree(clf0, 
         feature_names = data.feature_names,
         #["�ɹ�ħ����", "�ɹ�ħ��",  "���ٱ���", "������" ], 
         class_names=data.target_names,
         filled=True) #Ŭ�������� ��ĥ
plt.show()

from sklearn.tree import export_text
r = export_text(clf0, feature_names=iris['feature_names'])
print(r)