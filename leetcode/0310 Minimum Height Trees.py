#!/usr/bin/env python
# coding: utf-8

# In[1]:


#노드 개수와 무방향 그래프를 입력받아 트리가 최소 높이가 되는 루트의 목록 리턴


# In[3]:


n1 = 4
edges1 = [[1,0], [1,2], [1,3]]


# In[4]:


n2 = 6
edges2 = [[0,3], [1,3], [2,3], [4,3], [5,4]]


# In[6]:


#풀이 : 단계별 리프 노드 제거
#최소 높이를 구성하려면 가장 가운데에 있는 값이 루트여야 함
# = 리프 노드를 하나씩 제거해 나가면서 남아 있는 값을 찾으면 이 값이 가장 가운데에 있는 값이 될 것이고
#이 값을 루트로 했을 때 최소 높이를 구성할 수 있다는 뜻
import collections
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        # 양방향 그래프 구성
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        # 첫 번째 리프 노드 추가
        leaves = []
        for i in range(n + 1):
            if len(graph[i]) == 1:
                leaves.append(i)

        # 루트 노드만 남을 때까지 반복 제거
        # 리프 노드의 개수만큼 계속 빼나가면서 최종 2개 이하가 남을 때까지 반복
        # 마지막에 남은 값이 1개 혹은 2개일 수 있음
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves

