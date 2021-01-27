#!/usr/bin/env python
# coding: utf-8

# In[1]:


#이진 트리에서 두 노드 간 가장 긴 경로의 길이를 출력하라


# In[2]:


#풀이


# In[8]:


import collections
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #중첩 함수는 부모 함수의 변수를 자유롭게 읽어들일 수 있음
    #하지만 중첩 함수에서 부모 함수의 변수를 재할당하게 되면 참조 ID가 변경되어 별도의 로컬 변수로 선언됨
    #값이 숫자나 문자가 아니라 리스트나 딕셔너리 같은 자료형이라면 재할당 없이 조작이 가능
    longest: int = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            # 왼쪽, 오른쪽 각각 리프 노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 가장 긴 경로
            # left+right+2 = 거리
            self.longest = max(self.longest, left + right + 2)
            # 상태값
            return max(left, right) + 1

        dfs(root)
        return self.longest        


# In[6]:


root = TreeNode(1)
node_1 = TreeNode(2)
node_2 = TreeNode(3)
node_3 = TreeNode(4)
node_4 = TreeNode(5)


# In[7]:


root.left = node_1
root.right = node_2
node_1.left = node_3
node_1.right = node_4

