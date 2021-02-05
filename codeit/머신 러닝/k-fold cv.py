#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np

from sklearn import datasets
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

#경고 메시지 출력을 막는 코드
import warnings
warnings.simplefilter(action = 'ignore', category = FutureWarning)


# In[7]:


iris_data = datasets.load_iris()


# In[9]:


X = pd.DataFrame(iris_data.data, columns = iris_data.feature_names)
y = pd.DataFrame(iris_data.target, columns = ['Class'])


# In[10]:


logistic_model = LogisticRegression(max_iter = 2000)


# In[13]:


#경고메시지를 막고자 values.ravle()
#성능들의 평균 계산
np.average(cross_val_score(logistic_model, X, y.values.ravel(), cv = 5))

