#!/usr/bin/env python
# coding: utf-8

# In[1]:


#모든 부분 집합을 리턴하라


# In[18]:


nums = (1,2,3)


# In[19]:


#풀이1
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def dfs(index, path):
            result.append(path)
        
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])
        
        dfs(0, [])
        return result


# In[20]:


Solution().subsets(nums)


# In[25]:


#풀이2
import itertools
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return list(map(list,itertools.chain.from_iterable(itertools.combinations(nums, r) for r in range(len(nums) + 1))))


# In[26]:


Solution().subsets(nums)

