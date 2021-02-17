#!/usr/bin/env python
# coding: utf-8

# In[25]:


#문자열 S와 T를 입력받아 O(n)에 T의 모든 문자가 포함된 S의 최소 윈도우를 찾아라


# In[26]:


#collections.Counter의 기능을 이용하면 매우 편리하게 풀이할 수 있지만, 타임아웃이 발생하지는 않지만, 너무 느리게 실행됨
#아마도 Counter끼리 AND 연산으로 비교하는 과정이 내부적으로 매우 무거운 연산이기 때문으로 추측
#코딩 테스트나 실무에서 풀이하긴 어려움


# In[27]:


S = 'ADOBECODEBANC'
T = 'ABC'


# In[28]:


#풀이1
#브루트 포스로 풀이
#T의 문자는 3개이므로 슬라이딩 윈도우 사이즈 = 3
#시간 복잡도 제한 O(n)
#이 풀이는 O(n^2)이므로 타임아웃으로 풀리지 않음


import collections
from typing import List


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def contains(s_substr_lst: List, t_lst: List): #t의 문자를 하나씩 비교하며 슬라이딩 윈도우 내에 속한 문자를 제거하는 방식으로 포함 여부 판단
            
            #문자 제거
            for t_elem in t_lst:
                if t_elem in s_substr_lst:
                    s_substr_lst.remove(t_elem)
                else:
                    return False
            return True

        if not s or not t:
            return ''

        window_size = len(t)

        for size in range(window_size, len(s) + 1):
            for left in range(len(s) - size + 1):
                s_substr = s[left:left + size]
                if contains(list(s_substr), list(t)):
                    return s_substr
        return ''


# In[29]:


Solution().minWindow(S, T)


# In[30]:


#풀이2
#투 포인터, 슬라이딩 윈도우로 최적화
#투 포인터를 이용하면 풀이1의 시간 복잡도를 O(n)으로 줄일 수 있음
#계속 우측으로 이동하는 슬라이딩 윈도우이면서 적절한 위치를 찾았을 때 좌우 포인터의 크기를 좁혀 나가는 투 포인터로 풀이 가능

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t) #필요한 문자 각각의 개수
        missing = len(t) #필요한 문자의 전체 개수
        left = start = end = 0

        # 오른쪽 포인터 이동
        for right, char in enumerate(s, 1): #right는 1부터 시작(첫 문자의 인덱스가 0이 아닌 1)
            
            #현재 문자가 필요한 문자 need[char]에 포함되어 있다면 필요한 문자의 전체 개수 1 감소
            #해당 문자의 필요한 개수 need[char]도 1 감소
            #right를 늘려 나가면서 슬라이딩 윈도우의 크기가 점점 더 커지는 형태
            missing -= need[char] > 0
            need[char] -= 1

            # 필요 문자가 0이면 왼쪽 포인터 이동 판단
            if missing == 0:
                
                #왼쪽 보인터가 불필요한 문자를 가리키고 있다면 음수
                #0을 가리키는 위치까지 왼쪽 포인터 이동
                while left < right and need[s[left]] < 0: 
                    need[s[left]] += 1
                    left += 1

                if not end or right - left <= end - start:
                    start, end = left, right
                need[s[left]] += 1
                missing += 1
                left += 1
                #missing = 0이 될때까지의 오른쪽 포인터와 need[s[left]]가 0이 될 때까지의 왼쪽 포인터를 정답으로 간주
                #이 값은 더 작은 값을 찾을 때까지 유지하다가 가장 작은 값인 경우, 정답으로 슬라이싱 결과 리턴
        return s[start:end]


# In[6]:


Solution().minWindow(S, T)

