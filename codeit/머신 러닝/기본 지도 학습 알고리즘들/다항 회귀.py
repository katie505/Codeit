#!/usr/bin/env python
# coding: utf-8

# In[25]:


from sklearn.datasets import load_boston
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd


# In[13]:


boston_dataset = load_boston()


# In[14]:


boston_dataset.data


# In[15]:


boston_dataset.data.shape


# In[17]:


#다항 속성 만들기
#가설함수가 이차함수라고 가정
polynomial_transformer = PolynomialFeatures(2)


# In[18]:


polynomial_data = polynomial_transformer.fit_transform(boston_dataset.data)


# In[19]:


polynomial_data


# In[36]:


polynomial_data.shape


# In[37]:


polynomial_feature_names = polynomial_transformer.get_feature_names(boston_dataset.feature_names)


# In[38]:


polynomial_feature_names


# In[39]:


X = pd.DataFrame(polynomial_data, columns = polynomial_feature_names)


# In[40]:


X


# In[41]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


# In[42]:


y = pd.DataFrame(boston_dataset.target, columns = ['MEDV'])
y


# In[43]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 5)


# In[44]:


model = LinearRegression()


# In[45]:


model.fit(X_train, y_train)


# In[46]:


model.coef_


# In[47]:


model.intercept_


# In[48]:


y_test_prediction = model.predict(X_test)


# In[ ]:




