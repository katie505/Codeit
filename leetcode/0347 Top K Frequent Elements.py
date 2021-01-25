#!/usr/bin/env python
# coding: utf-8

# In[1]:


#k번 이상 등장하는 요소를 추출하라


# In[21]:


nums = [1, 1, 1, 2, 2, 3]
k = 2


# In[22]:


#풀이1
from typing import List
import collections
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        heap = []
        #힙에 삽입하는 방식
        #1. 파이썬 리스트에 모두 삽입한 다음 마지막에 heapify()
        #2. 매번 heappush()를 하는 방식 => 매번 heapify()가 일어나기 때문에 별도 처리 필요 없음
        
        #힙에 freqs의 키를 음수로 삽입 : 가장 빈도 수가 높은 값이 가장 작은 음수
        #힙은 키 순서대로 정렬되기 때문에 이를 위해 빈도 수를 키로 한 것
        #파이썬 heapq 모듈은 최소 힙만 지원
        for f in freqs:
            heapq.heappush(heap, (-freqs[f], f))
            
        topk = list()
        
        #k번만큼 추출, 최소 힙(Min Heap)이므로 가장 작은 음수 순으로 추출
        for _ in range(k):
            topk.append(heapq.heappop(heap)[1])
        
        return topk


# In[23]:


Solution().topKFrequent(nums, k)


# In[24]:


#풀이2
#Counter의 most_common() : 빈도 수가 높은 순서대로 아이템 추출
#튜플로 나오지만 리스트와 마찬가지로 모두 정답 처리 됨
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]


# In[25]:


Solution().topKFrequent(nums,k)

