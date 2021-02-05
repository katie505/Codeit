#!/usr/bin/env python
# coding: utf-8

# In[1]:


#부호없는 정수형을 입력받아 1비트의 개수를 출력하라


# In[13]:


#이 문제의 결과는 모두 0으로 구성된 비트들과의 해밍 거리로, 이를 해밍 가중치라고 부름
#이 문제의 정답은 해밍 가중치의 값


# In[8]:


n_1 = 11
n_2 = 128
n_3 = 4294967293


# In[9]:


#풀이1
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')


# In[14]:


#풀이2
#파이썬의 문자열 기능을 사용하지 않고 비트 연산만으로 1비트의 개수 계산
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            #1을 뺀 값과 AND 연산 횟수 측정
            #=> 할 때마다 비트가 1씩 빠지게 됨
            #0이 될 때까지 반복하면 전체 비트에서 1의 개수가 몇 개인지 알 수 있다
            #n이 0이 될 때까지 반복하고, 그 횟수를 리턴하면 그 값이 바로 1비트의 개수가 됨
            n &= n - 1
            count += 1
        return count


# In[10]:


Solution().hammingWeight(n_1)


# In[11]:


Solution().hammingWeight(n_2)


# In[12]:


Solution().hammingWeight(n_3)

