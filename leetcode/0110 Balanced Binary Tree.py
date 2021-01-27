#!/usr/bin/env python
# coding: utf-8

# In[8]:


#이진 트리가 높이 균형인지 판단하라
#높이 균형은 모든 노드의 서브 트리 간의 높이 차이가 1 이하인 것
#균형이 맞아야 효율적으로 트리를 구성할 수 있으며, 탐색 또한 훨씬 더 효율적으로 처리할 수 있기 때문
#높이 균형을 매번 맞추는 AVL 트리는 대표적인 자가 균형 이진 탐색 트리


# In[2]:


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# In[3]:


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(root):
            #맨 마지막 노드에 이르면 각각 left = 0, right = 0
            if not root:
                return 0
            
            #재귀 호출로 리프 노드까지 내려감
            left = check(root.left)
            right = check(root.right)
            
            # 높이 차이가 나는 경우 -1, 이외에는 높이에 따라 1 증가
            if left == -1 or                     right == -1 or                     abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return check(root) != -1


# In[4]:


root1 = TreeNode(3)
node1 = TreeNode(9)
node2 = TreeNode(20)
node3 = TreeNode(15)
node4 = TreeNode(7)
root1.left = node1
root1.right = node2
node2.left = node3
node2.right = node4


# In[5]:


root2 = TreeNode(1)
node5 = TreeNode(2)
node6 = TreeNode(2)
node7 = TreeNode(3)
node8 = TreeNode(3)
node9 = TreeNode(4)
node10 = TreeNode(4)
root2.left = node5
root2.right = node6
node5.left = node7
node5.right = node8
node7.left = node9
node7.right = node10


# In[6]:


Solution().isBalanced(root1)


# In[7]:


Solution().isBalanced(root2)

