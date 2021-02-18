#!/usr/bin/env python
# coding: utf-8

# In[1]:


#당신은 계단을 오르고 있다. 정상에 도달하기 위해 n 계단을 올라야 한다
#매번 각각 1계단 또는 2계단씩 오를 수 있다면 정상에 도달하기 위한 방법은 몇 가지 경로가 되는지 계산하라


# In[2]:


n = 3


# In[3]:


#풀이1
#타임아웃으로 풀리지 않음
#재귀 구조 브루트 포스(피보나치 수열과 완전히 동일한 풀이)
#이처럼 새로운 유형의 문제를 피보나치 수열 같은 기존의 유명한 문제와 연결해 풀이하는 방법은 문제 해결에 매우 좋은 방법
#면접관에게도 이 문제를 보면서 피보나치 수열을 떠올렸다고 얘기한다면 좋은 평가를 받을 수 있음

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# In[4]:


Solution().climbStairs(n)


# In[5]:


#풀이2
#메모이제이션
#피보나치 수와는 초깃값만 약간 다를 뿐 메모이제이션으로 풀이하는 방식은 동일
import collections

class Solution:
    dp = collections.defaultdict(int)

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.dp[n]


# In[6]:


Solution().climbStairs(n)

