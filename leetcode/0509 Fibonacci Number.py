#!/usr/bin/env python
# coding: utf-8

# In[1]:


#피보나치 수를 구하라


# In[2]:


#풀이1
#재귀 구조 브루트 포스
#가장 느림

class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.fib(N - 1) + self.fib(N - 2)


# In[3]:


#풀이2
#메모이제이션(다이나믹 프로그래밍의 하향식 풀이)
#재귀로 계산해 나가지만, 이미 계산한 값은 저장해뒀다가 바로 리턴
#한번 계산한 수는 더 이상 계산하지 않으므로 매우 효율적

import collections

class Solution:
    dp = collections.defaultdict(int)

    def fib(self, N: int) -> int:
        if N <= 1:
            return N

        if self.dp[N]:
            return self.dp[N]
        self.dp[N] = self.fib(N - 1) + self.fib(N - 2)
        return self.dp[N]


# In[4]:


#풀이3
#타뷸레이션 방식
#재귀를 사용하지 않고 반복으로 풀이하며, 작은 값부터 직접 계산하면서 타뷸레이션
#타뷸레이션이 일차원 선형 구조라 복잡하지 않고, 구조 자체도 단순해 이해가 쉬운편

class Solution:
    dp = collections.defaultdict(int)

    def fib(self, N: int) -> int:
        self.dp[1] = 1

        for i in range(2, N + 1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]
        return self.dp[N]


# In[5]:


#풀이4
#두 변수만 이용해 공간 절약
#메소드 바깥에 클래스의 멤버 변수도 선언할 필요가 없기 때문에 코드는 훨씬 더 간결해짐
#공간복잡도 O(n)에서 O(1)로 줄어듦
#시간복잡도는 동일

class Solution:
    def fib(self, N: int) -> int:
        x, y = 0, 1
        for i in range(0, N):
            x, y = y, x + y
        return x

