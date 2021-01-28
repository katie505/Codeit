#!/usr/bin/env python
# coding: utf-8

# In[1]:


#BST의 각 노드를 현재값보다 더 큰 값을 가진 모든 노드의 합을 만들어라


# In[3]:


root = TreeNode(4)
node1 = TreeNode(1)
node2 = TreeNode(6)
node3 = TreeNode(0)
node4 = TreeNode(2)
node5 = TreeNode(5)
node6 = TreeNode(7)
node7 = TreeNode(3)
node8 = TreeNode(8)


# In[4]:


root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node4.right = node7
node2.left = node5
node2.right = node6
node6.right = node8


# In[2]:


#풀이
#우측 자식 노드는 항상 부모 노드보다 큰 값인 점을 이용
#in-order순회에 해당 : 오른쪽 - 부모 - 왼쪽
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    val: int = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 중위 순회 노드 값 누적
        if root:
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)

        return root

