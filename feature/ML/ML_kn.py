# -*- coding: utf-8 -*-
from sklearn import datasets
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
import joblib

path = 'C:/MaliciousURL-Project/result/real/'
datasets = pd.read_csv(path + 'MLtest.csv',header=0)

X = datasets.iloc[:, 1:35]
y = datasets[['abnormal']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
'''
clf = DecisionTreeClassifier(
    max_depth=5,
    min_samples_split=3,
    min_samples_leaf=1,
    max_features=None,
    random_state=42)
'''
'''
clf = RandomForestClassifier(n_estimators=100,
    max_depth=16,
    min_samples_split=3,
    min_samples_leaf=1,
    max_features='sqrt',
    random_state=42)


'''
clf = ExtraTreesClassifier(n_estimators=100,
    max_depth=8,
    min_samples_split=3,
    min_samples_leaf=1,
    max_features='sqrt',
    random_state=42)



clf.fit(X_train, y_train)

#joblib.dump(clf,'C:/MaliciousURL-Project/result/real/knn_model_decision_tree.pkl')
#joblib.dump(clf,'C:/MaliciousURL-Project/result/real/knn_model_randomforest.pkl')
joblib.dump(clf,'C:/MaliciousURL-Project/result/real/knn_model_extra_tree.pkl')