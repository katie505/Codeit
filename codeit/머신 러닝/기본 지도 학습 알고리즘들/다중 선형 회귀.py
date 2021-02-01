#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.datasets import load_boston
import pandas as pd


# In[2]:


boston_dataset = load_boston()
print(boston_dataset.DESCR)


# In[3]:


boston_dataset.feature_names


# In[4]:


boston_dataset.data


# In[5]:


X = pd.DataFrame(boston_dataset.data, columns = boston_dataset.feature_names)


# In[6]:


X


# In[8]:


y = pd.DataFrame(boston_dataset.target, columns = ['MEDV'])


# In[10]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


# In[11]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 5)


# In[12]:


model = LinearRegression()


# In[13]:


model.fit(X_train, y_train)


# In[14]:


model.coef_


# In[16]:


model.intercept_


# In[17]:


y_test_prediction = model.predict(X_test)
y_test_prediction


# In[19]:


mean_squared_error(y_test, y_test_prediction) ** 0.5

