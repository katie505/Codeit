#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import GridSearchCV
from math import sqrt


# In[4]:


admission = pd.read_csv('admission_data.csv')

X = admission.drop('Chance of Admit ', axis = 1)

polynomial_transformer = PolynomialFeatures(2) #2차식 변형기 정의
polynomial_features = polynomial_transformer.fit_transform(X.values)

features = polynomial_transformer.get_feature_names(X.columns)

X = pd.DataFrame(polynomial_features, columns = features)
y = admission[['Chance of Admit ']]


# In[5]:


hyper_parameter = {
    'alpha' : [0.01, 0.1, 1, 10],
    'max_iter' : [100, 500, 1000, 1500, 2000]
}


# In[6]:


lasso_model = Lasso()


# In[7]:


hyper_parameter_tuner = GridSearchCV(lasso_model, hyper_parameter, cv = 5)


# In[8]:


hyper_parameter_tuner.fit(X, y)
#경고문은 max_iter값이 충분하지 않다는 내용
#= 원하는 최적점을 찾을 수 없었다


# In[9]:


hyper_parameter_tuner.best_params_

