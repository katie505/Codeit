#!/usr/bin/env python
# coding: utf-8

# In[1]:


#연결 리스트를 뒤집어라


# In[19]:


#풀이1
#재귀 구조로 뒤집기

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import List
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            #node가 None이 될 때까지 재귀 호출하면 마지막에는 백트래킹되면서 연결 리스트가 거꾸로 연결됨
            #여기서 맨 처음에 리턴된 prev는 뒤집힌 연결 리스트의 첫 번째 노드
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)


# In[29]:


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)


# In[26]:


s = Solution()
answer = s.reverseList(head)
while answer is not None:
    print(f'{answer.val} ->', end = " ")
    answer = answer.next


# In[30]:


#풀이2
#반복이 재귀에 비해 70% 수준의 메모리를 차지해 공간 복잡도는 좀 더 낮은 편이며, 실행 속도 또한 약간 더 빠른 편
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import List
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        
        #node.next를 이전 prev리스트로 계속 연결하면서 끝날 때까지 반복
        #node가 None이 될 때 prev는 뒤집힌 연결 리스트의 첫 번째 노드가 됨
        #prev에 node를, node에 next를 별도로 셋팅하며, 이를 이용해 node가 None이 될 때까지 계속 while 반복문을 돌게 된다
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        
        return prev


# In[31]:


s = Solution()
answer = s.reverseList(head)
while answer is not None:
    print(f'{answer.val} ->', end = " ")
    answer = answer.next

