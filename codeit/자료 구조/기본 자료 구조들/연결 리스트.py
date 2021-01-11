#!/usr/bin/env python
# coding: utf-8

# In[5]:


#노드 객체 만들기
class Node:
    """링크드 리스트의 노드 클래스"""
    
    def __init__(self, data):
        self.data = data #노드가 저장하는 데이터
        self.next = None #다음 노드에 대한 레퍼런스
        

# 데이터 2, 3, 5, 7, 11을 담는 노드 생성
head_node = Node(2)
node_1 = Node(3)
node_2 = Node(5)
node_3 = Node(7)
tail_node = Node(11)

# 노드들을 연결
head_node.next = node_1
node_1.next = node_2
node_2.next = node_3
node_3.next = tail_node

#노드 순서대로 출력
iterator = head_node
 
while iterator is not None:
    print(iterator.data)
    iterator = iterator.next


# In[14]:


#연결 리스트 클래스
class LinkedList:
    """연결 리스트 클래스"""
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def find_node_at(self, index):
        """연결 리스트 접근 연산 메소드. 파라미터 인덱스는 항상 있다고 가정"""
        iterator = self.head
        
        for _ in range(index): #iterator 변수를 이용해서 index번째에 있는 노드에 접근
            iterator = iterator.next #반복문을 돌때마다 다음 노드로 이동
            
        return iterator
    
    def append(self, data):
        """연결 리스트 추가 연산 메소드"""
        new_node = Node(data)
        
        #다른 노드들이랑 연결하기 위한 방법은 2가지
        #1. 연결리스트가 비어있을 때
        #2. 비어있지 않을 때
        #1) tail노드와 new 노드 연결
        #2) new 노드를 tail노드로 설정
        
        if self.head is None: #비어있을 때(= head 속성이 비어있음)
            self.head = new_node
            self.tail = new_node
        else: #비어있지 않을 때
            self.tail.next = new_node
            self.tail = new_node

    def __str__(self):
        """연결 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        # 연결 리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의
        iterator = self.head

        # 연결 리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += f" {iterator.data} |"
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str
#새로운 연결 리스트 생성
my_list = LinkedList()

#연결 리스트에 데이터 추가
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
my_list.append(11)

#노드 출력
iterator = my_list.head
 
while iterator is not None:
    print(iterator.data)
    iterator = iterator.next


# In[16]:


#연결 리스트 노드에 접근(데이터 가지고 오기)
#인덱스 3에 있는 데이터 가져오기
print(my_list.find_node_at(3).data) 

#연결 리스트 노드에 접근(데이터 바꾸기)
my_list.find_node_at(2).data = 13

print(my_list) #전체 연결 리스트 출력


# In[23]:


class Node:
   
    def __init__(self, data):
        self.data = data 
        self.next = None 
        
class LinkedList:
   
    def __init__(self):
        self.head = None  
        self.tail = None  
    
    def insert_after(self, previous_node, data): #특정 위치에 넣기
        """연결 리스트 주어진 노드 뒤 삽입 연산 메소드"""
        new_node = Node(data)
        
        if previous_node is self.tail: #가장 마지막 순서에 삽입
            previous_node.next = new_node
            self.tail = new_node
        else: #두 노드 사이에 삽입할 때
            new_node.next = previous_node.next
            previous_node.next = new_node
            
    def find_node_at(self, index):
        """연결 리스트 접근 연산 메소드. 파라미터 인덱스는 항상 있다고 가정"""
        iterator = self.head
        
        for _ in range(index): #iterator 변수를 이용해서 index번째에 있는 노드에 접근
            iterator = iterator.next #반복문을 돌때마다 다음 노드로 이동
            
        return iterator
    
    def delete_after(self, previous_node):
        """연결 리스트 삭제연산. 주어진 노드 뒤 노드를 삭제한다"""
        data = previous_node.next.data
        
        if previous_node.next is self.tail: # 지우려는 노드가 tail노드일 때
            previous_node.next=  None
            self.tail = previous_node
            
        else: #두 노드 사이 노드를 지울때
            previous_node.next = previous_node.next.next
        
        return data
    
    def prepend(self, data):
        """링크드 리스트의 가장 앞에 데이터 삽입"""
        # 코드를 쓰세요
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            
    def pop_left(self):
        """링크드 리스트의 가장 앞 노드 삭제 메소드. 단, 링크드 리스트에 항상 노드가 있다고 가정한다"""
        # 코드를 쓰세요
        data = self.head.data
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            
        return data
    
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  
            self.tail = new_node

    def __str__(self):
        """연결 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        # 연결 리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의
        iterator = self.head

        # 연결 리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += f" {iterator.data} |"
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str
        
linked_list = LinkedList()

# 연결 리스트에 데이터 추가
linked_list.append(2)
linked_list.append(3)
linked_list.append(5)
linked_list.append(7)

print(linked_list)

node_2 = linked_list.find_node_at(2) 
linked_list.insert_after(node_2, 6)
print(linked_list)

m_list = LinkedList()
m_list.append(2)
m_list.append(3)
m_list.append(5)
m_list.append(7)
m_list.append(11)

print(m_list)

node_3 = m_list.find_node_at(2)
m_list.delete_after(node_3)

print(m_list)


# In[25]:


my_list = LinkedList()

my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)

print(my_list)


# In[30]:


#더블리 연결 리스트 노드
class Node:
   
    def __init__(self, data):
        self.data = data 
        self.next = None
        self.prev = None
        
class LinkedList:
   
    def __init__(self):
        self.head = None  
        self.tail = None  
    
    def insert_after(self, previous_node, data):
        new_node = Node(data)
        
        if previous_node is self.tail: #가장 마지막 순서에 삽입
            new_node.prev = previous_node
            previous_node.next = new_node
            self.tail = new_node
        else: #두 노드 사이에 삽입할 때
            new_node.prev = previous_node
            new_node.next = previous_node.next
            previous_node.next.prev = new_node
            previous_node.next = new_node
            
    def find_node_at(self, index): #단순 연결 리스트와 동일
        iterator = self.head
        
        for _ in range(index): 
            iterator = iterator.next 
            
        return iterator
    
    def find_node_with_data(self, data): #단순 연결 리스트와 동일
        iterator = self.head
        
        while iterator is not None:
            if iterator.data == data:
                return iterator
            
            iterator = iterator.next
        return None
    
    def prepend(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
    def delete(self, node_to_delete):
        
        if node_to_delete is self.head and node_to_delete is self.tail:
            self.head = None
            self.tail = None
        elif node_to_delete is self.head:
            self.head = self.head.next
            self.head.prev = None
        elif node_to_delete is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev
        
        return node_to_delete.data
    
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  
            new_node.prev = self.tail
            self.tail = new_node
            

    def __str__(self): #단순 연결 리스트와 동일
        res_str = "|"

        iterator = self.head

        while iterator is not None:
            res_str += f" {iterator.data} |"
            iterator = iterator.next 

        return res_str


# In[33]:


# 새로운 링크드 리스트 생성
my_list = LinkedList()

# 새로운 노드 4개 추가
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)

print(my_list)

# 두 노드 사이에 있는 노드 삭제
node_at_index_2 = my_list.find_node_at(2)
my_list.delete(node_at_index_2)
print(my_list)

# 가장 앞 노드 삭제
head_node = my_list.head
print(my_list.delete(head_node))
print(my_list)

# 가장 뒤 노드 삭제
tail_node = my_list.tail
my_list.delete(tail_node)
print(my_list)


# In[ ]:




