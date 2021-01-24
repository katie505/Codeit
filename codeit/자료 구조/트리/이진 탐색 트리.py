#!/usr/bin/env python
# coding: utf-8

# In[1]:


#이진 탐색 트리 구현


# In[2]:


class Node:
    """이진 트리 노드"""
    #자식 노드, 부모 노드 모두 저장할 수 있음
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None        


# In[3]:


node_0 = Node(5)
node_1 = Node(3)
node_2 = Node(7)


# In[4]:


node_0.left_child = node_1
node_0.right_child = node_2

node_1.parent = node_0
node_2.parent = node_0


# In[5]:


def print_inorder(node):
        """주어진 노드를 in-order로 출력해주는 함수"""
        if node is not None:
            print_inorder(node.left_child)
            print(none.data)
            print_inorder(node.right_child)
            
class BinarySearchTree:
    """이진 탐색 트리 클래스"""
    def __init__(self):
        self.root = None
        
    def print_sorted_tree(self):
        """이진 탐색 트리 내의 데이터를 정렬된 순서로 출력해주는 메소드"""
        print_inorder(self.root)


# In[6]:


#비어 있는 이진 탐색 트리 생성
bst = BinarySearchTree()

