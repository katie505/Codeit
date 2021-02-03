#!/usr/bin/env python
# coding: utf-8

# In[16]:


#Min-Max Standardization


# In[3]:


import pandas as pd
import numpy as np

from sklearn import preprocessing


# In[6]:


data = pd.read_csv('NBA_player_of_the_week.csv')


# In[5]:


data.head()


# In[8]:


data.describe()


# In[9]:


height_weight_age_df = data[['Height CM', 'Weight KG', 'Age']]


# In[10]:


height_weight_age_df.head()


# In[11]:


scaler = preprocessing.MinMaxScaler()


# In[13]:


normalized_data = scaler.fit_transform(height_weight_age_df)
normalized_data


# In[14]:


normalized_df = pd.DataFrame(normalized_data, columns = ['Height', 'Weight', 'Age'])


# In[15]:


normalized_df.describe()


# In[17]:


#Standardization


# In[20]:


from sklearn import preprocessing
import pandas as pd
import numpy as np


# In[21]:


#소수점 5번째 자리 까지만 출력되도록 설정
pd.set_option('display.float_format', lambda x: '%.5f' %x)


# In[24]:


#표준화
scaler = preprocessing.StandardScaler()
standardized_data = scaler.fit_transform(height_weight_age_df)
standardized_df = pd.DataFrame(standardized_data, columns = ['Height', 'Weight', 'Age'])


# In[26]:


standardized_df.describe()


# In[33]:


data = pd.DataFrame([25000000, 35000000, 30000000, 50000000, 35000000], columns = ['Age'])


# In[34]:


data


# In[35]:


scaler = preprocessing.MinMaxScaler()


# In[36]:


normal = scaler.fit_transform(data)


# In[37]:


normal


# In[38]:


#One-hot Encoding
import pandas as pd


# In[42]:


data = pd.read_csv('titanic.csv')


# In[40]:


data


# In[43]:


titanic_sex_embarked = data[['Sex', 'Embarked']]


# In[44]:


titanic_sex_embarked.head()


# In[45]:


one_hot_encoded_df = pd.get_dummies(titanic_sex_embarked)


# In[47]:


one_hot_encoded_df.head()


# In[49]:


one_hot_encoded_df = pd.get_dummies(data = data, columns = ['Sex', 'Embarked'])


# In[51]:


one_hot_encoded_df.head()

