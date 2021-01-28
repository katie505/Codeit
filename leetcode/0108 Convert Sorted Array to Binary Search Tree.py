#!/usr/bin/env python
# coding: utf-8

# In[5]:


#오름차순으로 정렬된 배열을 높이 균형 이진 탐색 트리(BST)로 변환


# In[2]:


nums = [-10, -3, 0, 5, 9]


# In[8]:


#풀이
#BST는 이진 검색의 마법을 적용한 이진 트리
#따라서 정렬된 배열을 이진 검색으로 계속 쪼개 나가기만 하면 됨
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        mid = len(nums) // 2

        # 분할 정복으로 이진 검색 결과 트리 구성
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])

        return node

