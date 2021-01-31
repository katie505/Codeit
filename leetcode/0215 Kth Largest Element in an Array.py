#!/usr/bin/env python
# coding: utf-8

# In[1]:


#정렬되지 않은 배열에서 k번째 큰 요소 추출


# In[6]:


nums = [3,2,3,1,2,4,5,5,6]
k = 4


# In[2]:


#풀이1
import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = list()
        for n in nums:
            heapq.heappush(heap, -n)

        for _ in range(1, k):
            heapq.heappop(heap)

        return -heapq.heappop(heap)


# In[3]:


#풀이2
#모든 값을 꺼내서 푸시하지 않고도 한 번에 heapify하여 처리
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)


# In[4]:


#풀이3
#nlargest() : n번째 큰 값을 추출하는 기능
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1] #k번째만큼 큰 값이 가장 큰 값부터 순서대로 리스트로 리턴됨
        #마지막 인덱스 -1이 k번째 값이 됨


# In[5]:


#풀이4
#정렬을 이용한 풀이
#추가, 삭제가 빈번할 때는 heapq를 이용한 힙 정렬이 유용하지만 
#입력값이 고정되어 있을 때는 한 번 정렬하는 것만으로도 충분
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]


# In[8]:


Solution().findKthLargest(nums, k)

