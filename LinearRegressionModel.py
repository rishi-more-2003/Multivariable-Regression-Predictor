import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

def featurescaling(arr):
    return ((arr-np.min(arr))/(np.max(arr)-np.min(arr)))

def encoding(arr):
    for i in range(0,len(arr)):
        if arr[i]=="Petrol":
            arr[i]=4
        elif arr[i]=="Diesel":
            arr[i]=3
        elif arr[i]=="CNG":
            arr[i]=2
        else:
            arr[i]=1
    return featurescaling(arr)

#Data Collection and Cleaning
df=pd.read_csv('Toyota.csv',index_col=0,na_values=['??',"????"])

#Filling missing values
df['Age'].fillna(df['Age'].mean(),inplace=True)
df['KM'].fillna(df['KM'].mean(),inplace=True)
df['FuelType'].fillna(df['FuelType'].mode()[0],inplace=True)
df['HP'].fillna(df['HP'].mean(),inplace=True)

#Dropping unnecessary columns
df.drop('MetColor',axis=1,inplace=True)
df.drop('Doors',axis=1,inplace=True)

#Scaling and Encoding the required features 
df['Age']=featurescaling(df['Age'])
df['KM']=featurescaling(df['KM'])
df['FuelType']=encoding(df['FuelType'])
df['HP']=featurescaling(df['HP'])
df['CC']=featurescaling(df['CC'])
df['Weight']=featurescaling(df['Weight'])

#Creating target and predictor dataframes
X=df.drop('Price',axis=1)
y=df['Price']

#Splitting data into train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 42)

#Applying Regression Models

lr = LinearRegression()
lr.fit(X_train, y_train)

print('Linear Regression Train Score is : ' , lr.score(X_train, y_train))
print('Linear Regression Test Score is : ' , lr.score(X_test, y_test))

clf=Ridge(alpha=0.1)
clf.fit(X_train,y_train)

print('\nRidge Regression Train Score is : ' , clf.score(X_train, y_train))
print('Ridge Regression Test Score is : ' , clf.score(X_test, y_test))

ls=Lasso(alpha=0.1)
ls.fit(X_train,y_train)

print('\nLasso Regression Train Score is : ' , ls.score(X_train, y_train))
print('Lasso Regression Test Score is : ' , ls.score(X_test, y_test))

dt=DecisionTreeRegressor(max_depth=5)
dt.fit(X_train,y_train)

print("\nDecision Tree Regression Train Score is : " , dt.score(X_train, y_train))
print("Decision Tree Regression Test Score is : " , dt.score(X_test, y_test))

knn=KNeighborsRegressor(n_neighbors=10)
knn.fit(X_train,y_train)

print("\nKNN Regression Train Score is : " , knn.score(X_train, y_train))
print("KNN Regression Test Score is : " , knn.score(X_test, y_test))
