#!/usr/bin/env python
# coding: utf-8

# In[1]:


#서로 다른 정수를 입력받아 가능한 모든 순열을 리턴하라


# In[2]:


nums = [1,2,3]


# In[3]:


#풀이1
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            # 리프 노드일때 결과 추가
            if len(elements) == 0:
                results.append(prev_elements[:])

            # 순열 생성 재귀 호출
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return results


# In[5]:


#풀이1 - 1
#copy
#copy대신 복잡한 리스트는 deepcopy()로 처리
import copy
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            # 리프 노드일때 결과 추가
            if len(elements) == 0:
                results.append(copy.copy(prev_elements))

            # 순열 생성 재귀 호출
            for e in elements:
                next_elements = copy.copy(elements)
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return results


# In[6]:


Solution().permute(nums)


# In[7]:


#풀이2
#빨리 실행되지만 함수의 결과가 리스트 내 튜플이므로 리스트를 반환하도록 요구하기 때문에 변화해서 처리해야함
import itertools

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))


# In[9]:


Solution().permute(nums)

