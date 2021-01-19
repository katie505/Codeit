#!/usr/bin/env python
# coding: utf-8

# In[1]:


#다음의 기능을 제공하는 해시맵을 디자인하라


# In[7]:


#풀이
#개별 Chaining 방식을 이용한 해시 테이블 구현
import collections

# Definition for singly-linked list.
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    # 초기화
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    # 삽입
    def put(self, key: int, value: int) -> None:
        #나머지를 해시값으로 정함 
        index = key % self.size
        # 인덱스에 노드가 없다면 삽입 후 종료
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        # 인덱스에 노드가 존재하는 경우 연결 리스트 처리
        # 해시 충돌이 발생하는 경우
        p = self.table[index] #인덱스의 첫 번째 값
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        #에러 없이 정상적으로 진행되면 p.next에 새 노드가 생성되면서 연결됨
        p.next = ListNode(key, value)

    # 조회
    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1

        # 노드가 존재할때 일치하는 키 탐색
        # p.next로 탐색
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    # 삭제
    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return

        # 인덱스의 첫 번째 노드일때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # 연결 리스트 노드 삭제
        # prev는 이전 노드, p는 현재 노드
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next


# In[8]:


hashMap = MyHashMap()
hashMap.put(1,1)
hashMap.put(2,2)


# In[9]:


hashMap.get(1)


# In[10]:


hashMap.get(3)


# In[12]:


hashMap.put(2,1)


# In[13]:


hashMap.get(2)


# In[14]:


hashMap.remove(2)


# In[15]:


hashMap.get(2)

