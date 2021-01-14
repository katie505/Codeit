#!/usr/bin/env python
# coding: utf-8

# In[1]:


#인덱스m에서 n까지를 역순으로 만들어라. 인덱스 m은 1부터 시작


# In[6]:


#풀이
from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution():
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        #예외 처리
        if not head or m == n:
            return head
        
        #start : 변경이 필요한 지점의 바로 앞 지점을 가리킴
        #end : start.next
        #start와 end는 끝까지 값이 변하지 않는다
        root = start = ListNode(None)
        root.next = head
        #start, end 지정
        for _ in range(m - 1):
            start = start.next
        end = start.next
        
        #start와 end를 기준으로
        #반복하면서 노드 차례대로 뒤집기
        for _ in range(n - m):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        
        return root.next


# In[8]:


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
m = 2
n = 4
s = Solution()
answer = s.reverseBetween(l1, m, n)
while answer is not None:
    print(f'{answer.val} ->', end=" ")
    answer = answer.next

