#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

import pandas as pd


# In[3]:


iris_data = load_iris()

X = pd.DataFrame(iris_data.data, columns = iris_data.feature_names)
y = pd.DataFrame(iris_data.target, columns = ['class'])


# In[4]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 5)


# In[5]:


y_train = y_train.values.ravel()


# In[6]:


model = RandomForestClassifier(n_estimators = 100, max_depth = 4)


# In[7]:


model.fit(X_train, y_train)


# In[8]:


model.predict(X_test)


# In[9]:


model.score(X_test, y_test)


# In[17]:


#평균 지니 감소를 이용해서 속성 중요도 계산
import numpy as np
import matplotlib.pyplot as plt
importance = model.feature_importances_


# In[20]:


indices_sorted = np.argsort(importance)

plt.figure()
plt.title('Feature Importances')
plt.bar(range(len(importance)), importance[indices_sorted])
plt.xticks(range(len(importance)), X.columns[indices_sorted], rotation = 90)
plt.show()

