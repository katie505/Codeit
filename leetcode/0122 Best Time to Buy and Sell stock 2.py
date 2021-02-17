#!/usr/bin/env python
# coding: utf-8

# In[1]:


#여러 번의 거래로 낼 수 있는 최대 이익을 산출하라


# In[4]:


prices = [7,1,5,3,6,4]


# In[5]:


#풀이1
#그리디 알고리즘
#다음번의 등락 여부를 미리 알 수 있고 수수료도 없기 때문에 몇 번이든 거래 가능
#항상 이익을 내는 방향으로 몇번이든 사고팔고를 반ㅂ고하면 됨
#계속 오르는 경우라도 몇 번이든 사고팔 수 있기 때문에 매번 단계마다 이익을 취하는 탐욕 구조로 구현

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        # 값이 오르는 경우 매 번 그리디 계산
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                result += prices[i + 1] - prices[i]
        return result


# In[6]:


Solution().maxProfit(prices)


# In[3]:


#풀이2
#파이썬다운 방식

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 0보다 크면 무조건 합산
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))


# In[7]:


Solution().maxProfit(prices)

