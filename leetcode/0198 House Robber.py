#!/usr/bin/env python
# coding: utf-8

# In[1]:


#어느 집에서든 돈을 훔쳐올 수 있지만 경보 시스템 때문에 바로 옆집은 훔칠 수 없고 한 칸 이상 떨어진 집만 가능
#각 집에는 훔칠 수 있는 돈의 액수가 입력값으로 표기되어 있다. 훔칠 수 있는 가장 큰 금액을 출력하라


# In[4]:


nums_1 = [1,2,3,1]
nums_2 = [2,7,9,3,1]


# In[5]:


#풀이1
#타임아웃으로 풀리지 않음. 정답은 잘 나오지만 탐색 범위가 너무 많음
#재귀 구조 브루트 포스
#바로 옆집은 훔칠 수 없으니 현재 집과 옆집 숫자 중의 최댓값을 구하고, 한 집 건너집까지의 최댓값과 현재 집의 숫자값과의 합을 구해서 두 수 중 더 높은 값이 정답
#rob 함수를 중첩 함수로 처리

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def _rob(i: int) -> int: #내부 함수라는 의미 부여
            if i < 0:
                return 0
            return max(_rob(i - 1), _rob(i - 2) + nums[i])

        return _rob(len(nums) - 1)


# In[6]:


Solution().rob(nums_1)


# In[8]:


Solution().rob(nums_2)


# In[3]:


#풀이2
#타뷸레이션
#풀이1과 알고리즘은 동일하나 이미 계산한 값은 dp에 저장하고 두 번 이상 계산하지 않음
#순회 방식인 타뷸레이션이 좀 더 직관적이어서 이해하기 쉬운 편
#결과는 파이썬의 해시 테이블인 딕셔너리에 넣을 것인데, 원래 딕셔너리는 입력 순서가 유지되지 않았으나 파있너 3.7+부터는 입력 순서가 유지됨
#여기서는 낮은 버전에서도 순서가 유지될 수 있도록 명시적으로 collections.OrderedDict()로 선언해 풀이
import collections
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        dp = collections.OrderedDict()
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp.popitem()[1] #가장 마지막 아이템 추출

