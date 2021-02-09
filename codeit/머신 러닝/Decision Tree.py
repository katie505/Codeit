#!/usr/bin/env python
# coding: utf-8

# In[6]:


from sklearn.datasets import load_iris
import pandas as pd


# In[4]:


iris_data = load_iris()
print(iris_data.DESCR)


# In[7]:


X = pd.DataFrame(iris_data.data, columns = iris_data.feature_names)


# In[8]:


y = pd.DataFrame(iris_data.target, columns = ['class'])


# In[9]:


from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


# In[10]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 5)


# In[11]:


model = DecisionTreeClassifier(max_depth = 4)


# In[12]:


model.fit(X_train, y_train)


# In[13]:


model.predict(X_test)


# In[16]:


#모델 성능 평가
model.score(X_test, y_test)


# In[18]:


importances = model.feature_importances_


# In[19]:


import matplotlib.pyplot as plt
import numpy as np


# In[20]:


#결정 트리에서 각 속성들이 얼마나 중요하게 사용되었는지를 한 번에 확인할 수 있음
#꽃잎의 길이가 가장 중요함을 알 수 있음

indices_sorted = np.argsort(importances)

plt.figure()
plt.title('Feature Importances')
plt.bar(range(len(importances)), importances[indices_sorted])
plt.xticks(range(len(importances)), X.columns[indices_sorted], rotation = 90)
plt.show()

