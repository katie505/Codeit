#!/usr/bin/env python
# coding: utf-8

# In[1]:


#트리의 전위, 중위 순회 결과를 입력값으로 받아 이진 트리를 구축하라


# In[7]:


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]


# In[8]:


#풀이
#전위의 첫 번째 값은 부모 노드 = 전위 순회의 첫 번째 결과는 정확히 중위 순회 결과를 왼쪽과 오른쪽으로 분할시키는 역할
#중위 순회의 분할 정복 문제로 바꾸는 것
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            # 전위 순회 결과는 중위 순회 분할 인덱스
            index = inorder.index(preorder.pop(0))

            # 중위 순회 결과 분할 정복
            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[0:index])
            node.right = self.buildTree(preorder, inorder[index + 1:])

            return node


# In[9]:


root = Solution().buildTree(preorder, inorder)


# In[10]:


root.val


# In[12]:


root.left.val


# In[13]:


root.right.val

