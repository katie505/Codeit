#!/usr/bin/env python
# coding: utf-8

# In[1]:


#문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라


# In[1]:

#내 풀이
def reverseString(strs):
    l = int(len(strs)/2)
    
    for left in range(l):
        right = len(strs) - left - 1
        temp = strs[left]
        strs[left] = strs[right]
        strs[right] = temp
        
    return None
    


# In[2]:


#풀이1
#투 포인터 : 2개의 포인터를 이용해 범위를 조정해가며 풀이하는 방식
from typing import List

def reverseString(self, s:List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


# In[3]:


#풀이2
from typing import List

def reverseString(self, s:List[str]) -> None:
    s.reverse()



# In[3]:


s = ["h", "e", "l", "l", "o"]


# In[4]:


reverseString(s)


# In[5]:


s

