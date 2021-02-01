#!/usr/bin/env python
# coding: utf-8

# In[1]:


#연결 리스트를 O(nlogn)에 정렬하라


# In[11]:


#풀이1
#병합 정렬
#연결 리스트는 특성상 피벗을 고정된 위치로 지정할 수밖에 없고 입력값에 따라 성능의 편차가 심하므로, 병합 정렬로 구현 시도

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 두 정렬 리스트 병합
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1 or l2

    def sortList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head

        #런너 기법 활용
        #병합 정렬의 분할 정복을 위해 중앙을 분할해야함
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None

        #분할 재귀 호출
        #계속 재귀 호출을 해나가면 결국 연결 리스트는 단일 아이템으로 모두 쪼개짐
        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return self.mergeTwoLists(l1, l2)


# In[12]:


root = ListNode(4)
node1 = ListNode(2)
node2 = ListNode(1)
node3 = ListNode(3)


# In[13]:


root.next = node1
node1.next = node2
node2.next = node3


# In[14]:


answer = Solution().sortList(root)
while answer is not None:
    print(f'{answer.val} ->', end=" ")
    answer = answer.next


# In[15]:


#풀이2
#퀵 정렬은 입력값에 따라 성능의 편차가 크고 다루기가 까다롭기 때문에, 성능이 우수함에도 실무에서는 좀처럼 퀵 정렬을 사용하지 않는다.


# In[16]:


#풀이3
#내장 함수를 이용하는 실용적인 방법
#면접 시 화이트보드에 알고리즘을 작성해야 한다면, 이런 방식은 지양해야함
#면접관이 이 문제를 풀어보라고 한다면, 연결 리스트에서 퀵 정렬 적용의 어려움(피벗을 원하는 형태로 설정하기 어려우며 이미 정렬되어 있을 경우 계속해서 불균형 리스트로 나뉜다는 점)을 언급하면서
#병합 정렬을 설명하는 편이 가장 좋음
#병합 정렬로 충분히 설명하고 실무에서는 sort()함수를 이용하겠다는 점 어필하는 것도 굿
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 연결 리스트 -> 파이썬 리스트
        p = head
        lst: List = []
        while p:
            lst.append(p.val)
            p = p.next

        # 정렬
        lst.sort()

        # 파이썬 리스트 -> 연결 리스트
        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next
        return head

