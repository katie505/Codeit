#!/usr/bin/env python
# coding: utf-8

# In[6]:


#k개의 정렬된 리스트를 1개의 정렬된 리스트로 병합하라
#대부분의 우선순위 큐 풀이에는 거의 항상 heapq모듈을 사용함


# In[3]:


#풀이
from typing import List
import heapq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        root = result = ListNode(None)
        heap = []
    
        #각 연결 리스트의 루트를 힙에 저장 
        #연결 리스트 중 첫 번째와 두 번째의 루트가 각각 1로 동일
        #동일한 값은 headppush()함수에서 에러 발생하기 때문에 중복된 값을 구분할 수 있는 추가 인자 필요
        #headppush의 두번째 인자에 처음에는 value를 넣고 두번째로 index를 삽입하여 에러가 나지 않게 해줌
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
                
        #headpop()으로 값을 추출하면 가장 작은 노드의 연결 리스트부터 차례대로 나오게됨
        #결과를 result 노드에 하나씩 추가
        #k개의 연결 리스트가 모두 힙에 계속 들어 있어야 그중에서 가장 작은 노드가 항상 차례대로 나올 수 있음
        #=> 추출한 연결 리스트의 그 다음 노드는 다시 힙에 추가
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next


# In[5]:


l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l3 = ListNode(2)
l3.next = ListNode(6)

answer = Solution().mergeKLists([l1, l2, l3])
while answer is not None:
    print(f'{answer.val} ->', end = " ")
    answer = answer.next

