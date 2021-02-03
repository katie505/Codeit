#!/usr/bin/env python
# coding: utf-8

# In[1]:


#두 정수 a와 b의 합을 구하라. +또는 -연산자는 사용할 수 없다
#=> 비트 연산만으로 풀이해야 하는 문제


# In[2]:


a = 1
b = 2


# In[3]:


c = -2
d = 3


# In[4]:


#풀이1
#전가산기 구현
#풀이가 지나치게 어려움
  
class Solution:
    def getSum(self, a: int, b: int) -> int:
        #입력값을 32비트 정수로 가정했으므로 MASK는 OxFFFFFFFF로 함
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF
        
        #전처리
        #먼저 이진수로 변환
        #-> 이진수로 변환하면 앞에 0b 식별자가 항상 붙음 = 우리에게는 필요 없는 값
        #-> 슬라이싱으로 0b 식별자 없애기
        #-> & MASK는 음수 처리를 위해 2의 보수로 만들어주는 역할
        #zfill(32) : 비어있는 자리를 모두 0으로 채워서 32비트로 만들기
        a_bin = bin(a & MASK)[2:].zfill(32)
        b_bin = bin(b & MASK)[2:].zfill(32)
        
        #처리한 값을 뒷부분부터, 즉 낮은 자릿수부터 하나씩 전가산기를 통과하면서 결과 채워나가기
        #32비트로 가정했으므로, 32번 반복
        result = []
        carry = 0
        sum = 0
        for i in range(32):
            A = int(a_bin[31 - i])
            B = int(b_bin[31 - i])

            # 전가산기 구현
            Q1 = A & B
            Q2 = A ^ B
            Q3 = Q2 & carry
            sum = carry ^ Q2
            carry = Q1 | Q3

            result.append(str(sum))
        if carry == 1:
            result.append('1')
        
        # 초과 자릿수 처리
        result = int(''.join(result[::-1]), 2) & MASK
        
        # 음수 처리
        # 음수는 32번째 비트의 값, 즉 치상위 비트가 1인 경우
        #
        if result > INT_MAX:
            result = ~(result ^ MASK)

        return result


# In[5]:


#풀이2
#좀 더 간소한 구현
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF
        
        # 합, 자릿수 처리
        #a는 carry 값을 고려하지 않는 a와 b의 합이 담기게 하고
        #b는 자릿수를 올려가며 carry 값이 담기게 함
        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

        # 음수 처리
        if a > INT_MAX:
            a = ~(a ^ MASK)
        return a


# In[6]:


Solution().getSum(a, b)


# In[7]:


Solution().getSum(c,d)

