#!/usr/bin/env python
# coding: utf-8

# In[1]:


#연결 리스트를 홀수 노드 다음에 짝수 노드가 오도록 재구성하라. 공간 복잡도 O(1), 시간 복잡도 O(n)에 풀이하라


# In[3]:


#풀이
#제약이 없을 경우 연결 리스트를 리스트로 바꾸고 슬라이싱과 같은 함수를 사용하면 좀 더 쉽고 직관적이며 빠르게 풀 수 있음
#변수들은 n의 크기에 관계 없이 항상 일정하게 사용하기 땜누에 공간 복잡도 O(1)
from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution():
    def oddEvenList(self, head: ListNode) -> ListNode:
        #예외 처리
        if head is None:
            return None
        
        odd = head
        even = head.next
        even_head = head.next
        
        #반복하면서 홀짝 노드 처리
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
        
        #홀수 노드의 마지막을 짝수 헤드로 연결
        odd.next = even_head
        return head


# In[4]:


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)

l2 = ListNode(2)
l2.next = ListNode(1)
l2.next.next = ListNode(3)
l2.next.next.next = ListNode(5)
l2.next.next.next.next = ListNode(6)
l2.next.next.next.next.next = ListNode(4)
l2.next.next.next.next.next.next = ListNode(7)


# In[5]:


s = Solution()
answer = s.oddEvenList(l1)
while answer is not None:
    print(f'{answer.val} ->', end=" ")
    answer = answer.next


# In[6]:


s = Solution()
answer = s.oddEvenList(l2)
while answer is not None:
    print(f'{answer.val} ->', end=" ")
    answer = answer.next

