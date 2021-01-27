#!/usr/bin/env python
# coding: utf-8

# In[1]:


#동일한 값을 지닌 가장 긴 경로를 찾아라


# In[2]:


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# In[3]:


root1 = TreeNode(5)
node_1_1 = TreeNode(4)
node_2_1 = TreeNode(5)
node_3_1 = TreeNode(1)
node_4_1 = TreeNode(1)
node_5_1 = TreeNode(5)
root1.left = node_1_1
root1.right = node_2_1
node_1_1.left = node_3_1
node_1_1.right = node_4_1
node_2_1.right = node_5_1


# In[4]:


root2 = TreeNode(1)
node_1_2 = TreeNode(4)
node_2_2 = TreeNode(5)
node_3_2 = TreeNode(4)
node_4_2 = TreeNode(4)
node_5_2 = TreeNode(5)
root2.left = node_1_2
root2.right = node_2_2
node_1_2.left = node_3_2
node_1_2.right = node_4_2
node_2_2.right = node_5_2


# In[5]:


class Solution:
    result : int = 0
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if node is None:
                return 0

            # 존재하지 않는 노드까지 DFS 재귀 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 현재 노드가 자식 노드와 동일한 경우 거리 1 증가
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            # 왼쪽, 오른쪽 자식 노드간 거리의 합 최대값이 결과
            self.result = max(self.result, left + right)
            # 자식 노드 상태값 중 큰 값 리턴
            return max(left, right)

        dfs(root)
        return self.result


# In[6]:


Solution().longestUnivaluePath(root1)


# In[7]:


Solution().longestUnivaluePath(root2)

