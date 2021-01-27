#!/usr/bin/env python
# coding: utf-8

# In[9]:


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
from typing import List


# In[10]:


root = TreeNode(4)
node1 = TreeNode(2)
node2 = TreeNode(7)
node3 = TreeNode(1)
node4 = TreeNode(3)
node5 = TreeNode(6)
node6 = TreeNode(9)
root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
node2.right = node6


# In[15]:


#풀이1
#재귀 이용
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right =                 self.invertTree(root.right), self.invertTree(root.left)
            return root
        return None


# In[29]:


#풀이2
#반복 구조로 BFS
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = collections.deque([root])
        
        while queue:
            node = queue.popleft()
            #부모 노드부터 하향식 스왑
            if node:
                node.left, node.right = node.right, node.left
                
                queue.append(node.left)
                queue.append(node.right)
        return root


# In[32]:


#풀이3
#반복 구조로 DFS
#pre-order
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = collections.deque([root])
        
        while stack:
            node = stack.pop()
            #부모 노드부터 하향식 스왑
            if node:
                node.left, node.right = node.right, node.left
                
                queue.append(node.left)
                queue.append(node.right)
        return root


# In[34]:


#풀이4
#반복 구조로 DFS 후위 순회
#post-order
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = collections.deque([root])
        
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.left)
                stack.append(node.right)
                
                node.left, node.right = node.right, node.left
        return root

