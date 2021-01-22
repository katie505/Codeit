#!/usr/bin/env python
# coding: utf-8

# In[1]:


#파이썬으로 서버에 요청 보내기


# In[2]:


import requests #요청을 보내기 위해 사용하는 모듈


# In[5]:


page = requests.get('https://www.google.com')
type(page)


# In[6]:


#html 코드 출력
page.text

