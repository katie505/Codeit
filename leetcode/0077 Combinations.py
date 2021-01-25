#!/usr/bin/env python
# coding: utf-8

# In[2]:


#전체 수 n을 입력받아 k개의 조합을 리턴하라


# In[3]:


n = 4
k = 2


# In[6]:


#풀이1
from typing import List
import copy

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements, start: int, k: int):
            if k == 0:
                results.append(copy.deepcopy(elements))
                return

            # 자신 이전의 모든 값을 고정하여 재귀 호출
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return results


# In[8]:


Solution().combine(4,2)


# In[9]:


#풀이2
import itertools

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n+1), k))


# In[10]:


Solution().combine(4,2)

