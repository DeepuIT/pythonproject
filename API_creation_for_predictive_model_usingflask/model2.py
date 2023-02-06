###################################################################################
###################################################################################
# Regression part of the model for house prices data
#importing the necessary libraries


#importing the necessary libraries
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle
df = pd.read_csv('AgriLand_Nectar_perflower.csv',encoding= 'unicode_escape',infer_datetime_format=True)

#feature engineering
df.columns = ['species', 'location', 'habitat', 'id', 'bagging', 'rinsing','bagging_date', 'bagging_hour', 'collection_date', 'collection_hour','year', 'temp', 'hum', 'plant_no', 'flower_no', 'flower_age','flower_sex', 'sugarin24', 'sugarmaxin24']
df.drop(['species','location','id','year','plant_no','flower_no','collection_date','bagging_date'],axis = 1,inplace = True)
df['sugarin24'].fillna(df['sugarin24'].mean(),inplace = True)
df['sugarmaxin24'].fillna(df['sugarmaxin24'].mean(),inplace = True)
df['bagging_hour'] = [float(str(i).split(':')[0]) for i in df['bagging_hour']]
df['collection_hour'] = [float(str(i).split(':')[0]) for i in df['collection_hour']]
df['habitat'] = [1 if any([x in i for x in ['wet','grass','pond']]) else 0 for i in df['habitat']]
df['collection_hour'].fillna(df['collection_hour'].mean(),inplace = True)
df['temp'].fillna(df['temp'].mean(),inplace = True)
df['hum'].fillna(df['hum'].mean(),inplace = True)
df['bagging_hour'].fillna(df['bagging_hour'].mean(),inplace = True)
df.dropna(inplace = True)
features = pd.get_dummies(df.drop('sugarmaxin24', axis = 1),drop_first = True)
target = df['sugarmaxin24']

#splitting the dataset into train and test set
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size = 0.2, random_state = 0)

#creating a linear regression model
regressor = LinearRegression()

#fitting the model on the training set
regressor.fit(X_train, y_train)

#saving the model
pickle_out = open("model2.pkl","wb")
pickle.dump(regressor,pickle_out)
pickle_out.close()
