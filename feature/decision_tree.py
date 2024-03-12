# -*- coding: utf-8 -*-import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
from functools import reduce
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv('C:/MaliciousURL-Project/result/testfile.csv', encoding='utf-8')

'''
df.columns = ['url','netname','Creation_day','Update_day','Expiration_day','Expiration_Creation_day',
              'ttl','len_domain','len_path','len_parameter','len_tld',
              '%','$','=','@','?','&','#','.','_','-',';','{','}','[',']','|','+','*',
              'uppercase','digit_ratio','consonant_vowe','https','file_extension','urlshortening','abnormal'] 
'''
X=df.iloc[:,1:-2].values
y=df.iloc[:,-1:].values

X_train, X_test , y_train, y_test = train_test_split( X, y, test_size = 0.2, random_state = 1)

#Ʈ�� ����
dTreeAll = DecisionTreeClassifier(random_state=0)
dTreeAll.fit(X_train,y_train)
dTreeAll_pred = dTreeAll.predict(X_test)
dTreeAll.score(X_train,y_train)

#Ʈ�� ����(���� ���� -> ����ġ��)
dTreeLimit=DecisionTreeClassifier(max_depth=3, random_state=0)
dTreeLimit.fit(X_train, y_train)
dTreeLimit.score(X_train,y_train)

#Ʈ�� �ð�ȭ(���� ����)
feature_names = df.columns.tolist()
feature_names = feature_names[1:-2]
target_name = np.array(['0','1'])
print(target_name)

df_dot_data = tree.export_graphviz(dTreeAll,feature_names=)









##############���� �� ���� �Լ���################
#gini ��� ���ϱ�
def gini(df, label):
    D_len = df[label].count() # ������ ��ü ����
    # �� Ŭ������ Count�� ���� Generator ����
    count_arr = (value for key, value in df[label].value_counts().items())
    # reduce�� �̿��� �ʱⰪ 1���� �� Ŭ���� (count / D_len)^2 ����
    return reduce(lambda x, y: x - (y/D_len)**2 ,count_arr,1)

#��Ʈ���� ���
def entropy(target_col):
    elements, counts = np.unique(target_col, return_counts = True)
    entropy = -np.sum([(counts[i]/np.sum(counts))*np.log2(counts[i]/np.sum(counts)) for i in range(len(elements))])
    return entropy

#�����̵� ���
def InfoGain(data,split_attribute_name,target_name):

    # ��ü ��Ʈ���� ���
    total_entropy = entropy(data[target_name])
    print('Entropy(D) = ', round(total_entropy, 5))

    # ���� ��Ʈ���� ���
    vals,counts= np.unique(data[split_attribute_name],return_counts=True)
    Weighted_Entropy = np.sum([(counts[i]/np.sum(counts))*
                               entropy(data.where(data[split_attribute_name]==vals[i]).dropna()[target_name])
                               for i in range(len(vals))])
    print('H(', split_attribute_name, ') = ', round(Weighted_Entropy, 5))

    # �����̵� ���
    Information_Gain = total_entropy - Weighted_Entropy
    return Information_Gain