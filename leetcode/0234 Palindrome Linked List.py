#!/usr/bin/env python
# coding: utf-8

# In[1]:


#연결 리스트가 팰린드롬 구조인지 판별하라
#leetcode 기반


# In[38]:


#풀이1
#팰린드롬 여부를 판별하기 위해서는 앞뒤로 모두 추출할 수 있는 자료구조 필요
#연결 리스트를 리스트로 변환
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q: List = []

        if not head:
            return True

        node = head
        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next

        # 팰린드롬 판별
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True


# In[ ]:


#풀이2
#데크는 이중(더블) 연결 리스트 구조
#풀이1에 비해 데크의 명시적인 선언만으로 상당한 속도 개선 효과가 있음
#매우 간단하면서도 효율적인 최적화 방법
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #데크 자료형 선언
        q: Deque = collections.deque()
            
        if not head:
            return True
    
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next
            
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        
        return True


# In[ ]:


#풀이3 런너를 이용한 우아한 풀이
#데크로 구현한 풀이와 성능은 비슷하지만, 연결 리스트를 다른 자료형으로 변환하거나 편법을 사용하지 않고
#그 자리에서 바로 풀이함으로써 좀 더 연결 리스트답게 우아한 방식으로 풀 수 있었음
#런너 : 연결 리스트를 순회할 때 2개의 포인터를 동시에 사용하는 기법. 한 포인터가 다른 포인터보다 앞서게 하여 병합 지점이나 중간 위치, 길이 등을 파별할 때 유용하게 사용할 수 있음
#대개 fast runner가 연결 리스트의 끝에 도달하면, slow runner는 정확히 연결 리스트의 중간 지점을 가리키게 된다.
#fast runner를 이용해서 slow runner가 연결 리스트의 중간 지점에 멈추도록 하고, 
#slow runner는 연결 리스트를 탐색하면서 동시에 역순의 연결 리스트를 구성
#fast ruuner가 연결리스트 순회를 마치면 중간지점까지 역순의 연결 리스트가 만들어지고, 나머지 반과 해당 역순연결리스트를 비교해서 palindrome 여부 check
#=> 투포인터와 비슷한 포인트(반으로 쪼개서 양방향에서 접근)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None #reversed linked list
        slow = fast = head #두 개의 runer(초기값은 head node)
        
        #런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next: #fast running(slow runner가 딱 연결 리스트 중간까지 도달하도록 함)
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
            
        if fast: #연결 리스트가 홀수의 원소를 갖는 경우, 가운데 원소를 palindrome 체크에서 배제하도록 함
            slow = slow.next
            
        #팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev
    #palindrome이 아니어서 while loop를 탈출했다면 rev가 None이 아니므로 False일 것이고,
    #정상적으로 while이 종료되었다면 rev가 None이므로 True일 것(slow로 해도 상관x)

