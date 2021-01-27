#!/usr/bin/env python
# coding: utf-8

# In[1]:


#이진 트리를 배열로 직렬화하고, 반대로 역직렬화하는 기능을 구현하라
#즉 다음과 같은 트리는 [1,2,3,null,null,4,5] 형태로 직렬화할 수 있을 것이다


# In[2]:


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# In[4]:


root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(4)
node4 = TreeNode(5)
root.left = node1
root.right = node2
node2.left = node3
node2.right = node4


# In[16]:


#풀이
#이진 트리 데이터 구조는 논리적인 구조
#직렬화 : 이를 파일이나 디스크에 저장하기 위해서는 물리적인 형태로 바꿔줘야함
#반대는 역직렬화
#pickle이라는 직렬화 모듈을 기본으로 제공
#피클링(pickling) : 파이썬 객체의 계층 구조를 바이트 스트림으로 변경하는 작업

#직렬화는 가능하면 BFS 탐색 결과로 표현해서, 배열만 봐도 트리 형태를 직관적으로 떠올릴 수 있도록 이해하기 쉽게 구현
#BFS로 표현하면 순서대로 배치되기 때문에, DFS에 비해 매우 직관적
import collections

from typing import List
class Codec:
    # 직렬화
    def serialize(self, root: TreeNode) -> str:
        queue = collections.deque([root])
        result = ['#']
        # 트리 BFS 직렬화
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)

                result.append(str(node.val))
            else:
                result.append('#')
        return ' '.join(result)

    # 역직렬화
    def deserialize(self, data: str) -> TreeNode:
        # 예외 처리
        if data == '# #':
            return None

        nodes = data.split()

        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])
        index = 2
        # 빠른 런너처럼 자식 노드 결과 먼저 확인 후 큐 삽입
        while queue:
            node = queue.popleft()
            if nodes[index] != '#':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1

            if nodes[index] != '#':
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        return root


# In[17]:


Codec().serialize(root)


# In[10]:


Codec().deserialize(serial)

