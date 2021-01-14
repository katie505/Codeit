#!/usr/bin/env python
# coding: utf-8

# In[1]:


#역순으로 저장된 연결 리스트의 숫자를 더하라


# In[21]:


#풀이1 자료형 변환
#연결 리스트를 문자열로 이어 부틴 다음에 숫자로 변환하고, 이를 모두 계산한 후 다시 연결 리스트로 바꾸기
from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    #연결 리스트 뒤집기
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
            
        return prev
    
    #연결 리스트를 파이썬 리스트로 변환
    def toList(self, node: ListNode) -> List:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list
    
    #파이썬 리스트를 연결 리스트로 변환
    def toReversedLinkedList(self, result: str) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
            
        return node
    
    #두 연결 리스트의 덧셈
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))
        
        resultStr = int(''.join(str(e) for e in a)) +                     int(''.join(str(e) for e in b))
        
        #최종 계산 결과 연결 리스트 변환
        return self.toReversedLinkedList(str(resultStr))


# In[22]:


s = Solution()
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)


# In[23]:


answer = s.addTwoNumbers(l1, l2)
while answer is not None:
    print(f'{answer.val} ->', end=" ")
    answer = answer.next


# In[18]:


#풀이2
#논리 회로의 전가산기와 유사한 형태
#자리올림수(carry)를 구하는 것까지 가산기의 원리와 거의 동일
#자리올림수 : 덧셈 연산 또는 곱셈 연산의 결과로 생성된 값이 컴퓨터에서 표현할 수 있는 범위를 넘어서 다음 자리로 전달되는 경우, 전달되는 그 값
#자료형을 일일히 변환하던 풀이1에 비해 코드가 깔끔함. 성능 또한 비슷
from typing import List
class Solution():
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)
        
        carry = 0
        
        while l1 or l2 or carry:
            sum = 0
            #두 입력값의 합 계산
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
                
            #두 입력값의 연산을 수행하고 자릿수가 넘어갈 경우에는 자리올림수 설정
            #몫(자리올림수)과 나머지(값) 계산
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next
        
        return root.next


# In[14]:


d = Solution()
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
answer = d.addTwoNumbers(l1, l2)
while answer is not None:
    print(f'{answer.val} ->', end=" ")
    answer = answer.next

