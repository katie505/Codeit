#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import matplotlib.pyplot as plt


# In[6]:


def prediction(theta_0, theta_1, x):
    return theta_0 + theta_1*x


# In[7]:


def prediction_difference(theta_0, theta_1, x, y):
    return prediction(theta_0, theta_1, x) - y


# In[8]:


def gradient_descent(theta_0, theta_1, x, y, num_iterations, alpha):
    m = len(x)
    cost_list = []
    
    for i in range(num_iterations):
        error = prediction_difference(theta_0, theta_1, x, y)
        cost = (error@error) / (2*m)
        cost_list.append(cost)
        
        theta_0 = theta_0 - alpha*error.mean()
        theta_1 = theta_1 - alpha*(error*x).mean()
        
        if i % 10 == 0:
            plt.scatter(house_size, house_price)
            plt.plot(house_size, prediction(theta_0, theta_1, x), color = 'red')
            plt.show()
    return theta_0, theta_1, cost_list


# In[9]:


house_size = np.array([0.9, 1.4, 2, 2.1, 2.6, 3.3, 3.35, 3.9, 4.4, 4.7, 5.2, 5.75, 6.7, 6.9])
house_price = np.array([0.3, 0.75, 0.45, 1.1, 1.45, 0.9, 1.8, 0.9, 1.5, 2.2, 1.75, 2.3, 2.49, 2.6])


# In[10]:


th_0 = 2.5
th_1 = 0


# In[11]:


th_0, th_1, cost_list = gradient_descent(th_0, th_1, house_size, house_price, 200, 0.1)


# In[12]:


print(th_0, th_1)


# In[13]:


#경사하강법을 할수록 손실이 줄어듦을 확인할 수 있음
plt.plot(cost_list)


# In[2]:


#scikit-learn = sklearn


# In[3]:


from sklearn.datasets import load_boston


# In[4]:


boston_dataset = load_boston()


# In[5]:


print(boston_dataset.DESCR)


# In[6]:


boston_dataset.feature_names


# In[7]:


boston_dataset.data


# In[8]:


boston_dataset.data.shape


# In[9]:


boston_dataset.target


# In[10]:


boston_dataset.target.shape


# In[11]:


import pandas as pd


# In[12]:


x = pd.DataFrame(boston_dataset.data, columns = boston_dataset.feature_names)


# In[13]:


x


# In[17]:


#선형회귀에 쓸 자료 준비


# In[14]:


x = x[['AGE']]


# In[15]:


y = pd.DataFrame(boston_dataset.target, columns = ['MEDV'])


# In[16]:


y


# In[18]:


#학습, 평가 데이터 나누기


# In[19]:


from sklearn.model_selection import train_test_split


# In[26]:


x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2, random_state = 5)


# In[27]:


print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)


# In[28]:


#선형회귀 모델 학습


# In[29]:


from sklearn.linear_model import LinearRegression


# In[30]:


model = LinearRegression()


# In[31]:


model.fit(x_train, y_train)


# In[33]:


model.coef_


# In[34]:


model.intercept_


# In[35]:


#f(x) = 31.04617413 - 0.12402883x


# In[36]:


y_test_prediction = model.predict(x_test)


# In[37]:


y_test_prediction


# In[38]:


#MSE 구하기
from sklearn.metrics import mean_squared_error


# In[41]:


#모형으로 예측하면 8천달러 정도의 오차가 있을 수 있다
mean_squared_error(y_test, y_test_prediction) ** 0.5

