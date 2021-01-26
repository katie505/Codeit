#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#선형대수학이 머신 러닝에 필요한 이유
#머신 러닝을 할 때는 데이터를 일차식에 사용하는 경우가 많다
#-> 행렬을 이용하면 정돈된 형태로 효율적이게 계산을 할 수가 있다
#-> 선형 대수학은 일차식, 일차 함수, 행렬, 벡터를 다루는 학문이기 때문에 필수


# In[3]:


import numpy as np


# In[3]:


A = np.array([
    [1,-1,2],
    [3,2,2],
    [4,1,2],
    [7,5,6]
])


# In[4]:


B = np.array([
    [0,1],
    [-1,3],
    [5,2]
])


# In[6]:


#3*5 행렬(0과 1시이 값을 랜덤으로)
c = np.random.rand(3,5)


# In[11]:


D = np.zeros((2, 4))


# In[12]:


#외적곱
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

B = np.array([
    [0, 1, 2],
    [2, 0, 1],
    [1, 2, 0]
])


# In[13]:


A*B


# In[1]:


#행렬 연산


# In[4]:


A = np.array([
    [1,-1,2],
    [3,2,2],
    [4,1,2],
])


# In[5]:


B = np.random.rand(3,3)


# In[8]:


B


# In[6]:


A + B


# In[11]:


#행렬 곱(내적)
A @ B


# In[10]:


5 * A


# In[12]:


#외적
A*B


# In[15]:


#전치행렬
A_transpose = np.transpose(A)
#np.transpose(A) = A.T
A_trasponse = A.T


# In[14]:


A_transpose


# In[16]:


#단위행렬
I = np.identity(3)


# In[17]:


I


# In[18]:


A@I


# In[26]:


#역행렬
#역행렬이 없는 행렬의 경우 역행렬과 최대한 비슷한 효과를 낼 수 있는 행렬 반환
#linalg : Linear Algebra
#p = psuedo
A_inverse = np.linalg.pinv(A)
A_inverse


# In[25]:


A @ A_inverse

