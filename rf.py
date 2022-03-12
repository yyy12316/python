import pandas as pd
import numpy as np

#导入数据并拆分为训练集和测试集
filename = './churn.csv'
data = pd.read_csv(filename)
col_name = list(data.columns)#获取所有列名

x_col = col_name
col_drop=['State','Account Length','Area Code','Phone', 'Churn?']#一些无意义的列，以及标签列'Churn?'
for i in col_drop:
    x_col.remove(i)
#print(x_col)

#查看是否有缺失值
print(data.isnull().any())

#数据预处理
#查看变量的取值
data['Intl Plan'].value_counts()
data['VMail Plan'].value_counts()
data['Intl Plan']=data['Intl Plan'].map({'yes':1,'no':0})
data['VMail Plan']=data['VMail Plan'].map({'yes':1,'no':0})


#拆分数据集
from sklearn.model_selection import train_test_split
X = data[x_col]

y = data['Churn?']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.1,random_state=33)

#使用随机森林分类
from sklearn.ensemble import RandomForestClassifier

#不断增大基分类器数量，查看分类准确率变换过程，寻找最佳的基分类器数
from sklearn.model_selection import cross_val_score
score_lst = []
n = 200
for i in range(n):
    rfc = RandomForestClassifier(n_estimators=i+1)
    rfc_score = cross_val_score(rfc,X_train,y_train).mean()  #cv=10
    score_lst.append(rfc_score)
k = score_lst.index(max(score_lst)) + 1
print('最佳得分为{}，对应的基分类器数量为{}'.format(max(score_lst),k))
#运行结果：最佳得分为0.9583177518085698，对应的基分类器数量为98

#基分类器数量与对应的分类准确率变换过程可视化
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['Simhei']#正常显示中文
plt.figure(figsize=[20,5])
x=range(1,n+1)
y=score_lst
plt.plot(x,y)
plt.xlabel('基分类器数量k')
plt.ylabel('模型预测准确率')
plt.show()