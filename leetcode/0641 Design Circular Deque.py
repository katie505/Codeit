#!/usr/bin/env python
# coding: utf-8

# In[1]:


#다음 연산을 제공하는 원형 데크를 디자인하라


# In[ ]:


#풀이
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyCircularDeque:
    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0 #len : 현재 길이
        self.head.right, self.tail.left = self.tail, self.head

    # 이중 연결 리스트에 신규 노드 삽입
    # _ : 내부에서만 사용한다는 의미
    def _add(self, node: ListNode, new: ListNode):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new

    def _del(self, node: ListNode):
        n = node.right.right
        node.right = n
        n.left = node

    #데크 처음에 아이템 추가하고 성공할 경우 true 리턴
    def insertFront(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True
    
    #데크 마지막에 아이템 추가하고 성공할 경우 true 리턴
    def insertLast(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True
    
    #데크 처음에 아이템 삭제하고 성공할 경우 true 리턴
    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True
    
    #데크 마지막에 아이템 삭제하고 성공할 경우 true 리턴
    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True
    
    #데크 첫 아이템 추출
    def getFront(self) -> int:
        return self.head.right.val if self.len else -1
    
    #데크 마지막 아이템 추출
    def getRear(self) -> int:
        return self.tail.left.val if self.len else -1

    #데크가 비어있는지 여부 판별
    def isEmpty(self) -> bool:
        return self.len == 0
    
    #데크가 가득 차 있는지 여부 판별
    def isFull(self) -> bool:
        return self.len == self.k

