#!/usr/bin/env python
# coding: utf-8

# In[1]:


#t가 s의 애너그램인지 판별하라


# In[3]:


s1 = 'anagram'
t1= 'nagaram'


# In[9]:


s2 = 'rat'
t2 = 'car'


# In[5]:


#풀이
#두 이렵값의 정렬된 값 비교
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


# In[6]:


Solution().isAnagram(s1, t1)


# In[10]:


Solution().isAnagram(s2, t2)

