#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.datasets import load_iris


# In[2]:


iris = load_iris()


# In[5]:


print(iris.DESCR)


# In[8]:


import pandas as pd
X = pd.DataFrame(iris.data, columns = iris.feature_names)


# In[9]:


X


# In[21]:


y = pd.DataFrame(iris.target, columns = ['class'])


# In[22]:


y


# In[23]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


# In[24]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 5)


# In[25]:


y_train = y_train.values.ravel()


# In[26]:


y_train


# In[27]:


#solver = 모델을 최적화할때 사용할 알고리즘 선택
#max_iter = 최적화를 몇 번 할 지
model = LogisticRegression(solver = 'saga', max_iter = 2000)


# In[28]:


model.fit(X_train, y_train)


# In[29]:


model.predict(X_test)


# In[30]:


model.score(X_test, y_test)


# In[ ]:


model.score()

