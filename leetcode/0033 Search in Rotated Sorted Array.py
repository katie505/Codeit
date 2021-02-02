#!/usr/bin/env python
# coding: utf-8

# In[2]:


#특정 피벗을 기준으로 회전하여 정렬된 배열에서 target 값의 인덱스를 출력하라


# In[3]:


nums = [4,5,6,7,0,1,2]
target = 1


# In[5]:


#풀이
#피벗을 기준으로 한 이진 검색
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 예외 처리
        if not nums:
            return -1

        #최소값 찾아 피벗 설정
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left
        
        # 피벗 기준 이진 검색
        # 재귀가 아닌 반복으로 풀이
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_pivot = (mid + pivot) % len(nums) 
            #mod에 피벗만큼 이동하고 배열의 길이를 초과할 경우 모듈로 연산을 회전될 수 있도록 처리

            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot
        return -1


# In[6]:


Solution().search(nums, target)

