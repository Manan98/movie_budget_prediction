import csv
from sklearn.svm import SVR
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import explained_variance_score
from sklearn.linear_model import *
import random
import pickle
import os

current_dir = os.getcwd()

movies=np.genfromtxt('movies.csv',delimiter=',')
movies_label=np.genfromtxt('movies_label.csv',delimiter=',')
test_real=np.genfromtxt('a.csv',delimiter=',')
sum=0
counter=0
for x in range(200):
randomdata=range(0,3907)
randomset=random.sample(randomdata,400)
print(randomset)
test=[]
test_label=[]
train=movies[1:1000]
train_label=movies_label[1:1000]
for i in range(400):
        test.append(movies[randomset[i]])
        test_label.append(movies_label[randomset[i]])
        np.delete(train, np.s_[0:], axis=0)
        np.delete(train_label, np.s_[0:], axis=0)

knn=KNeighborsRegressor(5,weights='uniform')
knn.fit(train,train_label)
filename = 'finalized_model.sav'
pickle.dump(knn, open(filename, 'wb'))

result=knn.predict(test)
score=knn.score(train,train_label)

    clf=Ridge(alpha=1.0)
    clf.fit(train,train_label)
    result=clf.predict(test)

    clf=Lasso(alpha=10.0)
    clf.fit(train,train_label)
    result=clf.predict(test)

    clf=ElasticNet(random_state=0)
    clf.fit(train,train_label)
    result=clf.predict(test)

sum+=mean_squared_error(result,test_label)
counter+=1
sum/=counter
print (sum)
