#!/usr/bin/env python
# coding: utf-8

# In[7]:


#J는 보석이며, S는 갖고 있는 돌이다. S에는 보석이 몇 개나 있을까? 대소문자는 구분한다


# In[8]:


#풀이1
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        #freqs 해시 테이블 선언
        freqs = {}
        count = 0

        # 돌(S)의 빈도 수 계산
        # 돌의 모음인 S를 문자 단위로 하나씩 분리해 반복
        for char in S:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1

        # 보석(J)의 빈도 수 합산
        for char in J:
            if char in freqs:
                count += freqs[char]

        return count


# In[9]:


J = "aA"
S = "aAAbbbb"
Solution().numJewelsInStones(J, S)


# In[10]:


#풀이2
import collections

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        freqs = collections.defaultdict(int)
        count = 0

        # 비교 없이 돌(S) 빈도 수 계산
        for char in S:
            freqs[char] += 1

        # 비교 없이 보석(J) 빈도 수 합산
        for char in J:
            count += freqs[char]

        return count


# In[11]:


J = "aA"
S = "aAAbbbb"
Solution().numJewelsInStones(J, S)


# In[12]:


#풀이3
import collections

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        freqs = collections.Counter(S)  # 돌(S) 빈도 수 계산
        count = 0

        # 비교 없이 보석(J) 빈도 수 합산
        for char in J:
            count += freqs[char]

        return count


# In[13]:


J = "aA"
S = "aAAbbbb"
Solution().numJewelsInStones(J, S)


# In[14]:


#풀이4
#해시 테이블과는 관련이 없음
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(s in J for s in S)


# In[15]:


J = "aA"
S = "aAAbbbb"
Solution().numJewelsInStones(J, S)

