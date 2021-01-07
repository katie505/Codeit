#!/usr/bin/env python
# coding: utf-8

# In[1]:


#한 번의 거래로 낼 수 있는 최대 이익을 산출하라


# In[2]:


prices = [7, 1, 5, 3, 6, 4]


# In[10]:


#풀이1 브루트 포스
#타임아웃으로 풀리지 않는다

from typing import List

def maxProf(prices: List[int]) -> int:
    max_price = 0
    
    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price, max_price)
            
    return max_price


# In[11]:


maxProf(prices)


# In[8]:


#풀이2

from typing import List
import sys

def maxProf(prices: List[int]) -> int:
    #최댓값이 되어야 할 profit, 최솟값이 되어야 할 min_price
    #profit의 초깃값은 가장 작은 값, min_price의 초깃값은 가장 큰 값
    #=> 어떤 값이 들어오든 바로 교체될 수 있기 때문
    profit = 0
    min_price = sys.maxsize
    
    #최저점과 비교해 더 작을 경우 최솟값 갱신
    #현재 값과 최솟값과의 차이를 계산해 만약 더 클 경우 최대값 갱신
    #최솟값과 최댓값을 계속 갱신
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)
        
    return profit


# In[9]:


maxProf(prices)

