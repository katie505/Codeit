#!/usr/bin/env python
# coding: utf-8

# In[1]:


#연결 리스트를 삽입 정렬로 정렬하라


# In[11]:


#풀이1
#비효율적인 연산이 수행됨
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        #먼저, 삽입 정렬은 정렬을 해야 할 대상과 정렬을 끝낸 대상, 두 그릅으로 나눠 진행
        #head : 정렬을 해야 할 대상
        #cur : 정렬을 끝낸 대상
        #정렬을 해야 할 대상 head 반복
        
        #cur에는 정렬을 끝낸 연결 리스트 추가
        #parent는 계속 그 위치에 두어 사실상 루트를 가리키게 한다
        #정렬을 끝낸 cur는 이미 정렬된 상태이므로, 정렬을 해야 할 대상 head와 비교하면서 더 작다면 계속 cur.next를 이용해 다음으로 이동
        cur = parent = ListNode(None)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next

            cur = parent
            return cur.next


# In[14]:


#풀이2
#삽입 정렬의 비교 조건 개선
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # 초기값 변경
        cur = parent = ListNode(0)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next

            # 필요한 경우에만 cur 포인터가 되돌아가도록 처리
            if head and cur.val > head.val:
                cur = parent
        return parent.next


# In[15]:


head = ListNode(4)
node1 = ListNode(2)
node2 = ListNode(1)
node3 = ListNode(3)
head.next = node1
node1.next = node2
node2.next = node3


# In[16]:


answer = Solution().insertionSortList(head)
while answer is not None:
    print(f'{answer.val} ->', end=" ")
    answer = answer.next

