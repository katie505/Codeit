#!/usr/bin/env python
# coding: utf-8

# In[1]:


#0을 완료하기 위해서는 1을 끝내야 한다는 것을 [0,1] 쌍으로 표현하는 n개의 코스가 있다.
#코스 개수 n과 이 쌍들을 입력으로 받았을 때 모든 코스가 완료가능한지 판별하라


# In[ ]:


#그래프가 순환구조인지를 판별하는 문제로 풀이 가능
#순환구조라면 계속 뱅글뱅글 맴돌게 될 것이고, 해당 코스는 처리할 수 없기 때문


# In[15]:


numCourses = 2
prerequisites_1 = [[1,0]]
prerequisites_2 = [[1,0], [0,1]]
prerequisites_3 = [[1,0], [1,0]]
prerequisites_4 = [[0,1]]


# In[10]:


#풀이1
import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        # 그래프 구성
        # y는 복수 개로 구성할 수 있게 함
        for x, y in prerequisites:
            graph[x].append(y)
        
        #중복 값을 갖지 않으므로 set()집합 자료형으로 정함
        traced = set()

        def dfs(i):
            # 순환 구조이면 False
            if i in traced:
                return False

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            # 탐색 종료 후 순환 노드 삭제
            traced.remove(i)

            return True

        # 순환 구조 판별
        for x in list(graph): #list(graph) : key값 list
            if not dfs(x):
                return False

        return True


# In[25]:


#풀이2
#순환이 아니더라ㅗㄷ 복잡하게 서로 호출하는 구조로 그래프가 구성되어 있다면
#불필요하게 동잃나 그래프를 여러 번 탐색하게 될 수도 있음
#한번 방문했던 그래프는 두 번 이상 방문하지 않도록 무조건 True로 리턴하는 구조로 개선한다면
#탐색 시간을 획기적으로 줄일 수 있음

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        # 그래프 구성
        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()
        visited = set()

        def dfs(i):
            # 순환 구조이면 False
            if i in traced:
                return False
            # 이미 방문했던 노드이면 True
            if i in visited:
                return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            # 탐색 종료 후 순환 노드 삭제
            traced.remove(i)
            # 탐색 종료 후 방문 노드 추가
            visited.add(i)

            return True

        # 순환 구조 판별
        for x in list(graph):
            if not dfs(x):
                return False

        return True

