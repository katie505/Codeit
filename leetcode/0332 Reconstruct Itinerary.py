#!/usr/bin/env python
# coding: utf-8

# In[1]:


#[from, to]로 구성된 항공권 목록을 이용해 JFK에서 출발하는 여행 일정을 구성하라
#여러 일정이 있는 경우 사전 어휘 순으로 방문


# In[7]:


tickets1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]


# In[8]:


tickets2 = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]


# In[15]:


#풀이1
#큐 연산
import collections
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        #{'ATL' : ['JFK', 'SFO'], 'JFK' : ['ATL', 'SFO'], 'SFO' : ['ATL']}
        # 그래프 순서대로 구성
        for a, b in sorted(tickets):
            graph[a].append(b)

        route = []

        def dfs(a):
            # 첫 번째 값을 읽어 어휘순 방문
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)

        dfs('JFK')
        # 다시 뒤집어 어휘순 결과로
        return route[::-1]


# In[16]:


Solution().findItinerary(tickets1)


# In[17]:


Solution().findItinerary(tickets2)


# In[18]:


#풀이2
#스택 연산으로 큐 연산 최적화 시도
#pop()은 O(1)이지만 pop(0)은 0(n)
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        # 그래프 뒤집어서 구성
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        route = []

        def dfs(a):
            # 마지막 값을 읽어 어휘순 방문
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)

        dfs('JFK')
        # 다시 뒤집어 어휘순 결과로
        return route[::-1]


# In[ ]:


#풀이3
#일정 그래프 반복
#재귀가 아닌 동일한 구조 반복
#대부분의 재귀 문제는 반복으로 치환할 수 있으며, 스택으로 풀이 가능
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        # 그래프 순서대로 구성
        for a, b in sorted(tickets):
            graph[a].append(b)

        route, stack = [], ['JFK']
        while stack:
            # 반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())

        # 다시 뒤집어 어휘순 결과로
        return route[::-1]

