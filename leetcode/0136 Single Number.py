#!/usr/bin/env python
# coding: utf-8

# In[1]:


#딱 하나를 제외하고 모든 엘리먼트는 2개씩 있다. 1개인 엘리먼트를 찾아라


# In[2]:


nums_1 = [2,2,1]
nums_2 = [4,1,2,1,2]


# In[3]:


#풀이
#XOR(= 배타적 OR) 문제
#XOR : 입력 값이 서로 다르면 True, 서로 동일할 경우 False
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num #XOR = ^

        return result


# In[4]:


Solution().singleNumber(nums_1)


# In[5]:


Solution().singleNumber(nums_2)

