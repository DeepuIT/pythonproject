###################################################################################
###################################################################################
# Regression part of the model for house prices data
#importing the necessary libraries


#importing the necessary libraries
import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression,RidgeCV,Lasso
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor

#loading the dataset
df = pd.read_csv('Real_estate.csv')
df.drop('No',axis = 1,inplace = True)
df.transaction_date =[int(i) for i in df.transaction_date ]

#separating the independent and dependent variables
x2 = df.drop('house_price_of_unit_area',axis =1)
y2 = df.house_price_of_unit_area

#splitting into test and train sets
from sklearn.model_selection import train_test_split
x_train2, x_test2, y_train2, y_test2 = train_test_split(x2,y2,test_size=0.2,random_state=0)

#fitting the linear regression model

regressor = Lasso()
regressor.fit(x_train2,y_train2)

#saving the model
pickle_out = open("model2.pkl","wb")
pickle.dump(regressor,pickle_out)
pickle_out.close()