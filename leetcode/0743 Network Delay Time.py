#!/usr/bin/env python
# coding: utf-8

# In[1]:


#k부터 출발해 모든 노드가 신호를 받을 수 있는 시간을 계산하라. 불가능할 경우 -1을 리턴.
#입력값(u, v, w)는 각각 출발지, 도착지, 소요 시간
#전체 노드의 개수는 N


# In[2]:


times = [[2,1,1], [2,3,1], [3,4,1]]
N = 4
K = 2


# In[3]:


#풀이
#2가지 사항 판별
#1. 모든 노드가 신호를 받는 데 걸리는 시간 - 가장 오래 걸리는 노드까지의 최단 시간
#2. 모든 노드에 도달할 수 있는지 여부 - 모든 노드의 다익스트라 알고리즘 계산 값이 존재하는지 유무로 판별
#우선순위 큐를 최소 힙으로 구현한 모듈인 heapq를 사용하는 형태로 구현

import collections
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        # 그래프 인접 리스트 구성
        for u, v, w in times:
            graph[u].append((v, w))

        # 큐 변수: [(소요 시간, 정점)]
        Q = [(0, K)] #시작점에서 정점까지의 소요 시간
        dist = collections.defaultdict(int) 

        # 우선 순위 큐 최소값 기준으로 정점까지 최단 경로 삽입
        while Q:
            #Q는 우선순위 큐이므로 값이 계속 쌓이다가 낮은 값부터 하나씩 추출되면서(최소 힙) 제거됨
            #dist에 존재하지 않는다면 바로 dist 값으로 time과 node의 순서가 바뀌면서 입력됨
            time, node = heapq.heappop(Q)
            # dist에 node의 포함 여부부터 체크
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))

        # 모든 노드 최단 경로 존재 여부 판별
        # 전체 노드 개수만큼이 모두 dist에 있다면 모든 노드의 최단 경로를 구했다는 의미
        if len(dist) == N:
            return max(dist.values())
        return -1


# In[4]:


Solution().networkDelayTime(times, N, K)

