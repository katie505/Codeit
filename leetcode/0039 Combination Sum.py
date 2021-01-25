#!/usr/bin/env python
# coding: utf-8

# In[1]:


#숫자 집합 candidates를 조합하여 합이 target이 되는 원소를 나열하라. 각 원소는 중복 나열 가능하다


# In[6]:


candidates1 = [2,3,6,7]
target1 = 7
candidates2 = [2,3,5]
target2 = 8


# In[3]:


#풀이
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(csum, index, path):
            # 종료 조건
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return

            # 자신 부터 하위 원소 까지의 나열 재귀 호출
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return result


# In[4]:


Solution().combinationSum(candidates1, target1)


# In[7]:


Solution().combinationSum(candidates2, target2)

