#!/usr/bin/env python
# coding: utf-8

# In[1]:


#겹치는 구간을 병합하라


# In[2]:


#풀이
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        for i in sorted(intervals, key=lambda x: x[0]):
            #다음 아이템의 시작 값이 이전 아이템의 끝과 더 이상 겹치지 않게 된다면, 병합ㅇ르 멈추고
            #merged += i 이용해 새로운 아이템 추가
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged += i, #콤마는 중첩 리스트를 만들어주는 역할을 함
        return merged


# In[7]:


intervals = [[1,3],[2,6],[8,10],[15,18]]


# In[4]:


Solution().merge(intervals)

