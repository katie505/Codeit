#!/usr/bin/env python
# coding: utf-8

# In[2]:


#이진 트리의 최대 깊이 구하기


# In[4]:


#풀이
#BFS로 풀이
#BFS는 재귀가 아닌 반복 구조로 풀이할 수 있음
#BFS는 큐를 사용하여 구현

import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = collections.deque([root])
        depth = 0

        while queue:
            depth += 1
            # 큐 연산 추출 노드의 자식 노드 삽입
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
        # BFS 반복 횟수 == 깊이
        return depth


# In[6]:


root = TreeNode(3)
node_1 = TreeNode(9)
node_2 = TreeNode(20)
node_3 = TreeNode(15)
node_4 = TreeNode(7)


# In[7]:


root.left = node_1
root.right = node_2
node_2.left = node_3
node_2.right = node_4


# In[8]:


Solution().maxDepth(root)

