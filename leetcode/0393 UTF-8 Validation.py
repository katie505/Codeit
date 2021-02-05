#!/usr/bin/env python
# coding: utf-8

# In[1]:


#입력값이 UTF-8 문자열이 맞는지 검증하라
#UTF-8의 실제 조건을 그대로 묻는 문제이기 때문에 실용적이며, 따라서 실무에서도 얼마든지 활용할 수 있는 좋은 문제


# In[2]:


data_1 = [197, 130, 1]
data_2 = [235, 140, 4]


# In[3]:


#풀이
from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # 문자 바이트 만큼 10으로 시작 판별
        def check(size):
            for i in range(start + 1, start + size + 1):
                if i >= len(data) or (data[i] >> 6) != 0b10:
                    return False
            return True

        start = 0
        while start < len(data):
            # 첫 바이트 기준 총 문자 바이트 판별
            first = data[start] #첫 바이트
            #check() : 각각 해당 바이트의 문자가 맞는지 판별
            #- size를 파라미터로 받아 해당 사이즈만큼 바이트가 10으로 시작하는지 판별
            #ex) 3바이트 문자라고 판별했다면, 나머지 2바이트가 모두 10으로 시작하는지 판별
            if (first >> 3) == 0b11110 and check(3):
                start += 4
            elif (first >> 4) == 0b1110 and check(2):
                start += 3
            elif (first >> 5) == 0b110 and check(1):
                start += 2
            elif (first >> 7) == 0:
                start += 1
            else:
                return False
        return True


# In[4]:


Solution().validUtf8(data_1)


# In[5]:


Solution().validUtf8(data_2)

