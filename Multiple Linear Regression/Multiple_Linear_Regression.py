# -*- coding: utf-8 -*-
#libraries
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

#import dataset 
dataset = pd.read_csv ('C:\\salary_data.csv')
x=dataset.iloc [:,:-1].values
y=dataset.iloc [:,2].values


#encoding categorical data 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
x[:,1] = labelencoder.fit_transform(x[:,1])
onehotencoder = OneHotEncoder(categorical_features=[1])
x=onehotencoder.fit_transform(x).toarray()

#avoid dummy variable problem
x=x[:,1:]

# Split the targets into training/testing sets
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split (x,y,test_size= 1/5,random_state=0)

    
#feature scalling / Normalizing
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)

#fitting a linear regression model    
from sklearn.linear_model import LinearRegression
regressor= LinearRegression()
regressor.fit(x_train,y_train)
 
# prediction
y_pred = regressor.predict(x_test)

#visualising
plt.scatter(y_test,y_pred)
plt.xlabel("Test Salary ")
plt.ylabel("Prediction")
plt.title("Salary vs Predicted Salary")


