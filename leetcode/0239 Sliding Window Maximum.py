#!/usr/bin/env python
# coding: utf-8

# In[6]:


#배열 nums가 주어졌을 때 k 크기의 슬라이딩 윈도우를 오른쪽 끝까지 이동하면서 최대 슬라이딩 윈도우를 구하라
#전형적인 슬라이딩 윈도우 문제


# In[2]:


nums = [1,3,-1,-3,5,3,6,7]
k = 3


# In[3]:


#풀이1
#브루트 포스로 계산
#슬라이딩 윈도우를 우측으로 움직여 가며 max()로 최댓값 추출
#매번 윈도우의 최댓값을 계산하기 때문에 시간 복잡도 = O(n)
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return nums

        r = []
        for i in range(len(nums) - k + 1):
            r.append(max(nums[i:i + k]))

        return r


# In[4]:


#풀이2
#큐를 이용한 최적화
#풀이1에서 슬라이딩 윈도우를 한 칸씩 움직여야 하는 부분은 개선이 어려움
#max()를 계산하는 부분 최적화
#시간 복잡도는 줄일 수 없지만, 가급적 최댓값 계산을 최소화하기 위해 이전의 최댓값을 저장해뒀다가 한 칸씩 이동할 때 새 값에 대해서만 더 큰값인지 확인
#-> 최댓값이 윈도우에서 빠지게 되는 경우에만 다시 전체를 계산하는 형태로 개선
#선입선출 형태로 풀이할 수 있기 때문에 큐 사용

#이미 최댓값이 존재한다면 새로 추가된 값이 기존 최댓값보다 더 큰 경우에만 최댓값 교체
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        window = collections.deque()
        current_max = float('-inf') #음의 무한대
        for i, v in enumerate(nums):
            window.append(v)
            if i < k - 1:
                continue

            # 새로 추가된 값이 기존 최대값보다 큰 경우 교체
            if current_max == float('-inf'):
                current_max = max(window)
            elif v > current_max:
                current_max = v

            results.append(current_max)

            # 최대값이 윈도우에서 빠지면 초기화
            if current_max == window.popleft():
                current_max = float('-inf')
        return results


# In[5]:


Solution().maxSlidingWindow(nums, k)

