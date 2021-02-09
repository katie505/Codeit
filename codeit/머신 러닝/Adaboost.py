#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier

import pandas as pd


# In[4]:


iris_data = load_iris()

X = pd.DataFrame(iris_data.data, columns = iris_data.feature_names)
y = pd.DataFrame(iris_data.target, columns = ['class'])


# In[5]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 5)
y_train = y_train.values.ravel()


# In[6]:


model = AdaBoostClassifier(n_estimators = 100)


# In[7]:


model.fit(X_train, y_train)
model.predict(X_test)
model.score(X_test, y_test)


# In[9]:


importance = model.feature_importances_


# In[10]:


import matplotlib.pyplot as plt
import numpy as np


# In[11]:


indices_sorted = np.argsort(importance)
plt.figure()
plt.title('Feature Importances')
plt.bar(range(len(importance)), importance[indices_sorted])
plt.xticks(range(len(importance)), X.columns[indices_sorted], rotation = 90)
plt.show()

