#!/usr/bin/env python
# coding: utf-8

# In[1]:


#이진 탐색 트리가 주어졌을 때 L이상 R이하의 값을 지닌 노드의 합을 구하라


# In[4]:


root = TreeNode(10)
node1 = TreeNode(5)
node2 = TreeNode(15)
node3 = TreeNode(3)
node4 = TreeNode(7)
node5 = TreeNode(18)
root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node2.right = node5
L = 7
R = 15


# In[5]:


#풀이1
#재귀 이용
#브루트 포스
#입력값이 매우 클 경우 브루트 포스와 가지치기의 속도 차이가 훨씬 더 큼
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0

        return (root.val if L <= root.val <= R else 0) +                self.rangeSumBST(root.left, L, R) +                self.rangeSumBST(root.right, L, R)


# In[7]:


#풀이2
#DFS 가지치기로 필요한 노드 탐색
#이진 탐색 트리는 왼쪽이 항상 작고, 오른쪽이 항상 크다
#현재 노드가 L보다 작을 경우, 더 이상 왼쪽을 탐색할 필요 없음
#현재 노드가 R보다 클 경우, 더 이상 오른쪽을 탐색할 필요 없음
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def dfs(node: TreeNode):
            if not node:
                return 0

            if node.val < L:
                return dfs(node.right)
            elif node.val > R:
                return dfs(node.left)
            return node.val + dfs(node.left) + dfs(node.right)

        return dfs(root)


# In[14]:


#풀이3
#반복구조 DFS로 필요한 노드 탐색
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        stack, sum = [root], 0
        # 스택 이용 필요한 노드 DFS 반복
        while stack:
            node = stack.pop()
            if node:
                if node.val > L:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
                if L <= node.val <= R:
                    sum += node.val
        return sum


# In[13]:


#풀이4
#반복 구조 BFS로 필요한 노드 탐색
#데크를 사용해야 성능을 높일 수 있지만, 편의상 간단히 리스트를 그냥 pop(0) 처리로 구현
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        stack, sum = [root], 0
        # 큐 연산을 이용해 반복 구조 BFS로 필요한 노드 탐색
        while stack:
            node = stack.pop(0)
            if node:
                if node.val > L:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
                if L <= node.val <= R:
                    sum += node.val
        return sum


# In[12]:


Solution().rangeSumBST(root, L, R)

