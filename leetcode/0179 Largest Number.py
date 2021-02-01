#!/usr/bin/env python
# coding: utf-8

# In[2]:


#항목들을 조합하여 만들 수 있는 가장 큰 수를 출력하라


# In[3]:


nums_1 = [10, 2]
nums_2 = [3, 30, 34, 5, 9]


# In[4]:


#풀이
#각 요소 단위로 크기 순으로 정렬하면 됨
#맨 앞에서부터 자릿수 단위로 비교해서 크기 순으로 정렬

from typing import List

class Solution:
    # 문제에 적합한 비교 함수
    @staticmethod
    #함수의 결과가 True라면 위치 변경이 이뤄져야 함
    def to_swap(n1: int, n2: int) -> bool:
        return str(n1) + str(n2) < str(n2) + str(n1)

    # 삽입 정렬 구현
    def largestNumber(self, nums: List[int]) -> str:
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j - 1], nums[j]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
            i += 1

        return str(int(''.join(map(str, nums))))


# In[5]:


Solution().largestNumber(nums_1)


# In[6]:


Solution().largestNumber(nums_2)

