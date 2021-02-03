#!/usr/bin/env python
# coding: utf-8

# In[1]:


#정렬된 배열을 받아 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라
#이 문제에서 배열은 0이 아닌 1부터 시작하는 것으로 한다


# In[3]:


nums = [2,7,11,15]
target = 9


# In[8]:


#풀이1
#투 포인터

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while not left == right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return left + 1, right + 1  # 리턴 값 +1(1부터 시작하므로)


# In[5]:


#풀이2
#이진 검색
#이진 검색 log n을 n번 반복하므로 시간 복잡도는 O(nlogn)
#투 포인터에 비해 2배 가량 늦음

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            left, right = k + 1, len(numbers) - 1
            expected = target - v
            # 이진 검색으로 나머지 값 판별
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] < expected:
                    left = mid + 1
                elif numbers[mid] > expected:
                    right = mid - 1
                else:
                    return k + 1, mid + 1


# In[6]:


#풀이3
#bisect + 슬라이싱 제거
import bisect
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            #왼쪽 범위를 제한하는 파라미터인 lo를 찾아냈고, 이 값을 지정하는 것으로 풀이
            i = bisect.bisect_left(numbers, expected, k + 1)
            if i < len(numbers) and numbers[i] == expected:
                return k + 1, i + 1


# In[9]:


Solution().twoSum(nums, target)

