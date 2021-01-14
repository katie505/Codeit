#!/usr/bin/env python
# coding: utf-8

# In[1]:


#연결 리스트를 입력받아 페어 단위로 스왑하라


# In[4]:


#풀이1
#노드 구조는 그대로 유지하되 값만 변경하는 방법
#실용성과는 다소 거리가 있음.
#변칙적인 풀이 방법이므로, 좋지 않은 피드백을 받을 가능성이 있다.

from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        

class Solution():
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head
        
        while cur and cur.next:
            #값만 교환
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
            
        return head


# In[5]:


s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

answer = s.swapPairs(head)
while answer is not None:
    print(f'{answer.val} ->', end=" ")
    answer = answer.next


# In[6]:


#풀이2

from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        

class Solution():
    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            #b가 a(head)를 가리키도록 할당
            b = head.next
            head.next = b.next
            b.next = head
            
            #prev가 b를 가리키도록 할당
            prev.next = b
            
            #다음번 비교를 위해 이동
            #3,4가 4,3으로 바꼈을 때 1,2쪽의 2를 4와 연결시키기 위해서는 prev가 꼭 필요하고 매 반복마다 순간 바꿔줘야함
            head = head.next
            prev = prev.next.next
            
        return root.next


# In[7]:


s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

answer = s.swapPairs(head)
while answer is not None:
    print(f'{answer.val} ->', end=" ")
    answer = answer.next


# In[8]:


#풀이3
#공간 복잡도가 낮다 : 불필요한 변수를 사용하지 않으묘
from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        

class Solution():
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            #스왑된 값 리턴 받음
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        
        return head


# In[9]:


s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

answer = s.swapPairs(head)
while answer is not None:
    print(f'{answer.val} ->', end=" ")
    answer = answer.next

