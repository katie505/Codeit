#!/usr/bin/env python
# coding: utf-8

# In[1]:


#각각의 사람은 (h, k)의 두 정수 쌍을 갖음
#h : 사람의 키
#k : 앞에 줄 서 있는 사람들 중 자신의 키 이상인 사람들의 수
#이 값이 올바르도록 줄을 재정렬하는 알고리즘 작성하라


# In[7]:


people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]


# In[4]:


#풀이
#우선순위 큐 이용

#우선순위 큐 자체가 매번 그때그때의 최소 또는 최댓값을 추출하기 때문에, 그리디에 어울리는 대표적인 자료구조라 할 수 있음
#실제로 그리디 문제의 대부분은 우선순위 큐를 활용해 풀이함

import heapq
from typing import List

#첫번째 값이 큰 순서대로 추출되는 최대 힙 형태로 풀이
#두번째 값은 삽입되는 인덱스로 활용
#파이썬은 최소 힙만 지원하기 때문에 첫 번째 값을 음수로 변경해 최대 힙 구현 가능

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        # 키 역순, 인덱스 삽입
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))

        result = []
        # 키 역순, 인덱스 추출
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])
        return result

