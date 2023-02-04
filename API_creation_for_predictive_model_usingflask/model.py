
#importing necessary libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle

#loading the dataset
dataset = pd.read_csv("iris.csv")

#separating independent and dependent variables
X = dataset.drop(['Id','Species'],axis = 1)
y = dataset['Species']

#splitting the data into train and test
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.3,random_state = 42)

#creating the model
model = LogisticRegression()

#fitting the model
model.fit(X_train,y_train)

#saving the model
pickle_out = open("model.pkl","wb")
pickle.dump(model,pickle_out)
pickle_out.close()
