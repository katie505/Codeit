#!/usr/bin/env python
# coding: utf-8

# In[1]:


#정렬된 nums를 입력받아 이진 검색으로 target에 해당하는 인덱스를 찾아라


# In[2]:


#이진 검색
#- 정렬된 배열에서 타겟을 찾는 검색 알고리즘
#- 값을 찾아내는 시간 복잡도가 O(log n)이라는 점에서 대표적인 로그 시간 알고리즘
#- 이진 탐색 트리와도 유사한 점이 많음
#실제 코딩 테스트 시에는 가급적 '재귀'나 '반복'으로 직접 이진 검색을 풀이하는 편이 나중에 코드 리뷰를 하게 되는 경우 더 좋은 평가를 받을 수 있음


# In[3]:


nums = [-1, 0, 3, 5, 9, 12]
target = 9


# In[6]:


#풀이1
#재귀 풀이
#절반씩 범위를 줄여나가며 맞출 때까지 계속 재귀 호출
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    return binary_search(mid + 1, right)
                elif nums[mid] > target:
                    return binary_search(left, mid - 1)
                else:
                    return mid
            else:
                return -1

        return binary_search(0, len(nums) - 1)


# In[7]:


#풀이2
#반복 풀이
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1


# In[8]:


#풀이3
#이진 검색 모듈 bisect
#여러 가지 예외 처리를 포함한 이진 검색 알고리즘이 깔끔하게 모듈 형태로 구현됨

import bisect
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1


# In[9]:


#풀이4
#이진 검색을 사용하지 않는 index 풀이
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1


# In[5]:


Solution().search(nums, target)

