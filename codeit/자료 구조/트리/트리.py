#!/usr/bin/env python
# coding: utf-8

# In[2]:


#이진 트리 구현


# In[9]:


class Node:
    """이진 트리 노드 클래스"""
    
    def __init__(self, data):
        """데이터와 두 자식 노드에 대한 레퍼런스를 갖는다"""
        self.data = data
        self.left_child = None
        self.right_child = None        


# In[10]:


root_node = Node(2)
node_B = Node(3)
node_C = Node(5)
node_D = Node(7)
node_E = Node(11)


# In[11]:


root_node.left_child = node_B
root_node.right_child = node_C

node_B.left_child = node_D
node_B.right_child = node_E


# In[12]:


test_node_1 = root_node.left_child
print(test_node_1.data)


# In[13]:


test_node_2 = test_node_1.right_child
print(test_node_2.data)

