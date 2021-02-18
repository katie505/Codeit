#!/usr/bin/env python
# coding: utf-8

# In[1]:


#합이 최대가 되는 연속 서브 배열을 찾아 합을 리턴하라


# In[ ]:


#투 포인터로 풀이하기 어려움
#연속된 서브 배열을 찾아야 하는 문제인 만큼 정렬을 할 수 없고, 다음 숫자가 뭐가 될지 모르는 상황에서 단순히 음수를 건너 뛰는 방식으로는 구현이 어려움


# In[3]:


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


# In[4]:


#풀이1
#메모이제이션
#앞에서부터 계속 값을 계산하면서 누적 합 계산
#이전 값을 계속 더해나가되 0이하가 되면 버림
#메모이제이션으로 값을 더해 나간 sums에서 최댓값을 추출하면 서브 배열의 최댓값을 찾을 수 있음

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
        return max(nums)


# In[5]:


Solution().maxSubArray(nums)


# In[ ]:


#풀이2
#카데인 알고리즘 : O(n)에 풀이가 가능하도록 고안한 알고리즘
#최대 서브 배열을 찾기 위해 어디서 시작되는지를 찾는 문제 O(n^2) 풀이에서 각 단계마다 최댓값을 담아 어디서 끝나는지를 찾는 문제 O(n) 풀이로 치환해서 풀이

import sys
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = -sys.maxsize
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)

        return best_sum


# In[6]:


Solution().maxSubArray(nums)

