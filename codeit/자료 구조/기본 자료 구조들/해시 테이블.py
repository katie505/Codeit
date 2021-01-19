#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Chaining에서 사용하는 연결 리스트


# In[17]:


#이중 연결 리스트 이용
class Node:
    def __init__(self, key, value):
        #기존의 변수 data 대신 key와 value
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    #탐색 메소드
    #특정 key를 갖는 노드 찾기
    def find_node_with_key(self, key):
        iterator = self.head
        
        while iterator is not None:
            if iterator.key == key:
                return iterator
            
            iterator = iterator.next
            
        return None
    
    #추가(맨 뒤 삽입) 메소드
    #data 변수 대신 key와 value를 받음
    def append(self, key, value):
        new_node = Node(key, value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
    #삭제 메소드
    def delete(self, node_to_delete):

        # 링크드 리스트에서 마지막 남은 데이터를 삭제할 때
        if node_to_delete is self.head and node_to_delete is self.tail:
            self.tail = None
            self.head = None

        # 링크드 리스트 가장 앞 데이터 삭제할 때
        elif node_to_delete is self.head:
            self.head = self.head.next
            self.head.prev = None

        # 링크드 리스트 가장 뒤 데이터 삭제할 떄
        elif node_to_delete is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None

        # 두 노드 사이에 있는 데이터 삭제할 때
        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev
            
    def __str__(self):
        res_str = ""

        # 링크드 리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드 리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += "{}: {}\n".format(iterator.key, iterator.value)
            iterator = iterator.next # 다음 노드로 넘어간다

        return res_str


# In[18]:


myList = LinkedList()


# In[19]:


myList.append(101, '최지웅')
myList.append(204, '강영훈')
myList.append(305, '성태호')


# In[21]:


print(myList)

