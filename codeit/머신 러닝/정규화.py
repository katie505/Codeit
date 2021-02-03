#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
import numpy as np

from math import sqrt

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures


# In[6]:


data = pd.read_csv('admission_data.csv').drop('Serial No.', axis = 1)


# In[7]:


data.head()


# In[13]:


X = data.drop('Chance of Admit ', axis = 1)
polynomial_transformer = PolynomialFeatures(6)
polynomial_features = polynomial_transformer.fit_transform(X.values)
features = polynomial_transformer.get_feature_names(X.columns)

X = pd.DataFrame(polynomial_features, columns = features)
X.head()


# In[15]:


y = data[['Chance of Admit ']]
y.head()


# In[16]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 5)


# In[17]:


model = LinearRegression()


# In[18]:


model.fit(X_train, y_train)


# In[19]:


y_train_predict = model.predict(X_train)


# In[20]:


y_test_predict = model.predict(X_test)


# In[21]:


#과적합

mse = mean_squared_error(y_train, y_train_predict)
print("training set에서의 성능")
print("-----------------------")
print(sqrt(mse))

mse = mean_squared_error(y_test, y_test_predict)
print("test set에서의 성능")
print("-----------------------")
print(sqrt(mse))


# In[26]:


#Lasso 모델
#Lasso 모델은 자체적으로 feature scaling을 할 수 있음
model = Lasso(alpha = 0.001, max_iter = 1000, normalize = True) # alpha = 람다 / max_iter = 경사하강법 반복 횟수
model.fit(X_train, y_train)


# In[27]:


y_train_predict = model.predict(X_train)
y_test_predict = model.predict(X_test)


# In[28]:


#과적합

mse = mean_squared_error(y_train, y_train_predict)
print("training set에서의 성능")
print("-----------------------")
print(sqrt(mse))

mse = mean_squared_error(y_test, y_test_predict)
print("test set에서의 성능")
print("-----------------------")
print(sqrt(mse))

