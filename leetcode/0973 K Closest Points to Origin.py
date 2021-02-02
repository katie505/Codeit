#!/usr/bin/env python
# coding: utf-8

# In[1]:


#평면상에 points 목록이 있을 때, 원점에서 K번 가까운 점 목록을 순서대로 출력하라
#평면상 두 점의 거리는 유클리드 거리로 한다


# In[2]:


#풀이
#유클리드 거리의 우선순위 큐 순서
import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(heap, (dist, x, y))

        result = []
        for _ in range(K):
            (dist, x, y) = heapq.heappop(heap)
            result.append((x, y))
        return result


# In[4]:


points_1 = [[1,3],[-2,2]]
K_1 = 1


# In[5]:


points_2 = [[3,3],[5,-1],[-2,4]]
K_2 = 2


# In[6]:


Solution().kClosest(points_1, K_1)


# In[7]:


Solution().kClosest(points_2, K_2)

