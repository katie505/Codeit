#!/usr/bin/env python
# coding: utf-8

# In[1]:


# n개의 페어(서로 겹치지 않는 쌍)를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수 출력


# In[3]:


nums = [1,4,3,2]


# In[17]:


#풀이1
from typing import List
 
def arrayPairSum(nums: List[int]) -> int:
    sum = 0
    pair = []
    nums.sort()
    #내림차순 nums.reverse()
    
    for n in nums:
        #앞에서부터 오름차순으로 페어를 만들어서 합 계산
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = [] #빈 pair로 만들고 다시 시작
    
    return sum


# In[23]:


#풀이2
#정렬된 상태에서 짝수 번째 인덱스의 값은 항상 작은 값
from typing import List
 
def arrayPairSum(nums: List[int]) -> int:
    sum = 0
    nums.sort()
    
    for i, n in enumerate(nums):
        if i % 2 == 0:
            sum += n
            
    return sum


# In[24]:


#풀이3
from typing import List
 
def arrayPairSum(nums: List[int]) -> int:
    #[::2] : 2칸씩 건너뛰는 것
    return sum(sorted(nums)[::2])

