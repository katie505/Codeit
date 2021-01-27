#!/usr/bin/env python
# coding: utf-8

# In[1]:


#두 이진 트리를 병합하라. 중복되는 노드는 값을 합산한다


# In[2]:


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# In[3]:


root1 = TreeNode(1)
node_1 = TreeNode(3)
node_2 = TreeNode(2)
node_3 = TreeNode(5)
root1.left = node_1
root1.right = node_2
node_1.left = node_3


# In[4]:


root2 = TreeNode(2)
node_4 = TreeNode(1)
node_5 = TreeNode(3)
node_6 = TreeNode(4)
node_7 = TreeNode(7)
root2.left = node_4
root2.right = node_5
node_4.right = node_6
node_5.right = node_7


# In[7]:


#풀이
from typing import List

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
            
            return node
        else:
            return root1 or root2


# In[9]:


root3 = Solution().mergeTrees(root1, root2)


# In[10]:


print(root3.val)


# In[11]:


print(root3.left.val)


# In[12]:


print(root3.right.val)

