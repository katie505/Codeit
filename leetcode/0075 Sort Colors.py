#!/usr/bin/env python
# coding: utf-8

# In[1]:


#빨간색을 0, 흰색을 1, 파란색을 2라 할 때 순서대로 인접하는 제자리 정렬을 수행하라


# In[9]:


#풀이
#네덜란드 국기 문제를 응용한 풀이
#네덜란드 국가의 색깔인 붉은색, 흰색, 파란색을 세 부분으로 대입해 분활하는 것
#피벗보다 작은 부분, 같은 부분, 큰 부분 이렇게 세 부분으로 분할하여 기존 퀵 정렬의 두 부분 분할에 비해 개선하는 방안
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, white, blue = 0, 0, len(nums)

        while white < blue:
            if nums[white] < 1:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] > 1:
                blue -= 1
                nums[white], nums[blue] = nums[blue], nums[white]
            else:
                white += 1


# In[10]:


nums = [2,0,2,1,1,0]


# In[12]:


Solution().sortColors(nums)
nums

