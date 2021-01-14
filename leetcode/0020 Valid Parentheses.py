#!/usr/bin/env python
# coding: utf-8

# In[1]:


#괄호로 된 입력값이 올바른지 판별하라


# In[3]:


#풀이
from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')':'(',
            '}':'{',
            ']':'[',
        }
        
        #스택 이용 예외 처리 및 일치 여부 판별
        #팝 결과가 일치하지 않는지 확인하는 것 외에도 스택이 비어 있는지 여부 함께 확인
        for i in s:
            if i not in table: 
                stack.append(i)  
            elif not stack or table[i] != stack.pop():
                return False
        return len(stack) == 0 


# In[5]:


str = '()[]{}'
fail = ')[](}{'
s = Solution()
s.isValid(str)
s.isValid(fail)

