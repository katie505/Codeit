#!/usr/bin/env python
# coding: utf-8

# In[1]:


#두 노드 간 값의 차이가 가장 작은 노드의 값의 차이를 출력하라


# In[2]:


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# In[3]:


root1 = TreeNode(4)
node11 = TreeNode(2)
node21 = TreeNode(6)
node31 = TreeNode(1)
node41 = TreeNode(3)
root1.left = node11
root1.right = node21
node11.left = node31
node11.right = node41


# In[4]:


root2 = TreeNode(10)
node12 = TreeNode(4)
node22 = TreeNode(15)
node32 = TreeNode(1)
node42 = TreeNode(8)
root2.left = node12
root2.right = node22
node12.left = node32
node12.right = node42


# In[5]:


#풀이1
#재귀로 중위순회
import sys

class Solution:
    prev = -sys.maxsize
    result = sys.maxsize

    # 재귀 구조 중위 순회 비교 결과
    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left:
            self.minDiffInBST(root.left)

        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.minDiffInBST(root.right)

        return self.result


# In[7]:


Solution().minDiffInBST(root1)


# In[8]:


Solution().minDiffInBST(root2)


# In[ ]:


#풀이2
#반복 구조로 중위 순회
#재귀와 달리 반복 구조에서는 한 함수 내에서 처리할 수 있기 때문에 함수 내 변수로 선언 가능
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        prev = -sys.maxsize
        result = sys.maxsize

        stack = []
        node = root

        # 반복 구조 중위 순회 비교 결과
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            result = min(result, node.val - prev)
            prev = node.val

            node = node.right

        return resultㅣ

