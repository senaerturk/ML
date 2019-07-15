import boto3
import re
import pandas as pd
import matplotlib.pyplot as plt

# Define IAM role
from sagemaker import get_execution_role
role = get_execution_role()

#taking s3 data
bucket='wordsdataset'
data_key = 'wordsData.csv'
data_location = 's3://{}/{}'.format(bucket, data_key)


dataset = pd.read_csv(data_location)
x=dataset.iloc [:,:-1].values
y=dataset.iloc [:,1].values


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split (x,y,test_size= 1/3,random_state=0)

#fitting a linear regression model   
from sklearn.linear_model import LinearRegression
regressor= LinearRegression()
regressor.fit(x_train,y_train)
    
y_pred = regressor.predict(x_test)
plt.scatter(x_train,y_train,color='yellow')
plt.plot(x_train,regressor.predict(x_train), color ='blue')
plt.title('Word Length vs Word Duration(Training set)')
plt.xlabel('Word Length')  
plt.ylabel('Word Duration')  
plt.show()  

#Visualising the Test set results
plt.scatter(x_test,y_test,color='red')
plt.plot(x_train, regressor.predict(x_train),color='blue')
plt.title('Word Length vs Word Duration(Test set)')
plt.xlabel('Word Length')
plt.ylabel('Word Duration')
plt.show()

