#!/usr/bin/env python
# coding: utf-8

# In[1]:


#두 정수를 입력받아 몇 비트가 다른지 계산하라


# In[2]:


x = 1
y = 4


# In[3]:


#풀이
#해밍 거리 = 두 정수 또는 두 문자열의 차이
# 문자열의 경우 해밍 거리는 다른 자리의 문자 개수가 되며, 이진수의 경우 다른 위치의 비트 개수
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1') #XOR 결과는 정수가 나오므로 이진수로 변경하고 여기서 1의 전체 개수를 헤아리면 = 해밍 거리 값


# In[4]:


Solution().hammingDistance(x, y)

