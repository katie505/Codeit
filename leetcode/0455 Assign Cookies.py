#!/usr/bin/env python
# coding: utf-8

# In[1]:


#아이들에게 1개씩 쿠키를 나눠줘야 함
#각 아이 child_i마다 그리드 팩터를 갖고 있으며, 이는 아이가 만족하는 최소 쿠키의 크기
#각 쿠키는 쿠키를 갖고 있으며, 크키는 그리드 팩터보다 크거나 같아야 아이가 만족하며 쿠키를 받음
#최대 몇 명의 아이들에게 쿠키를 줄 수 있는지 출력하라


# In[2]:


g_1 = [1,2,3]
s_1 = [1,1]


# In[3]:


g_2 = [1,2]
s_2 = [1,2,3]


# In[4]:


#풀이1
#그리디 알고리즘
#그리디하게 배분하면 쉽게 풀 수 있는 문제
#예제는 모든 입력값이 정렬되어 있지만, 원래 문제에는 정렬된 값이라는 제약이 없기 때문에 먼저 정렬해주는 작업 직접 진행
#2개의 리스트 모두 번갈아가며 탐색

from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        child_i = cookie_j = 0
        # 만족하지 못할 때까지 그리디 진행
        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                child_i += 1
            cookie_j += 1

        return child_i


# In[5]:


Solution().findContentChildren(g_1, s_1)


# In[6]:


Solution().findContentChildren(g_2, s_2)


# In[9]:


#풀이2
#이진 검색
#하나의 리스트를 순회하면서 다른 하나는 이진 검색으로 찾기
#그 다음 인덱스가 현재 부여한 아이들보다 클 경우에는 이 경우 더 줄 수 있다는 뜻
#줄 수 있는 아이들의 수를 1명 더 늘림

import bisect
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        result = 0
        
        #기존 이진 검색 시 bisect_left() 사용 = 찾아낸 값의 해당 위치 인덱스 리턴
        #bisect_right()는 left와 기능이 동일하며 찾아낸 값의 다음 인덱스를 리턴함
        for i in s:
            # 이진 검색으로 더 큰 인덱스 탐색
            index = bisect.bisect_right(g, i)
            if index > result:
                result += 1
        return result


# In[10]:


Solution().findContentChildren(g_1, s_1)


# In[11]:


Solution().findContentChildren(g_2, s_2)

