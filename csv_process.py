import csv
from sklearn.svm import SVR
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import explained_variance_score
from sklearn.linear_model import LogisticRegression
import tensorflow as tf



train=np.genfromtxt('train_2.csv',delimiter=',')
train_label=np.genfromtxt('train_label.csv',delimiter=',')
train.reshape(3008,4)
train_label.reshape(3008,1)

test=np.genfromtxt('train_2.csv',delimiter=',')
test_label=np.genfromtxt('test_label.csv',delimiter=',')
"""

knn=KNeighborsRegressor(1,weights='uniform')
knn.fit(train,train_label)
result=knn.predict(test)
score=knn.score(train,train_label)

#print (score)
with open('result.csv','w',newline='') as f:
    writer=csv.writer(f,dialect='excel')
    for i in range(len(test_label)):
        writer.writerow([test_label[i],result[i]])


"""
x=tf.placeholder
