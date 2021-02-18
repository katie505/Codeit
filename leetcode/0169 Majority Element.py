#!/usr/bin/env python
# coding: utf-8

# In[1]:


#과반수를 차지하는(절반은 초과하는) 엘리먼트를 출력하라


# In[5]:


nums_1 = [3,2,3]
nums_2 = [2,2,1,1,1,2,2]


# In[6]:


#풀이1
#브루트 포스로 비교
#앞에서부터 하나씩 과반수를 넘는지 일일이 체크하다가 과반수를 넘으면 바로 정답으로 처리
# 타임아웃 발생

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) > len(nums) // 2:
                return num


# In[7]:


#풀이2
#브루트 포스를 다이나믹 프로그래밍으로 최적화
#동일한 알고리즘으로 연산 횟수만 줄이기

#nums.count()로 한 번 카운트를 계산한 값은 저장해서 재활용
#만약 계산되지 않았던 값이 들어온다면 항상 0이 될 것이고, 그 때만 카운트 계산
#'메모이제이션'을 이용한 매우 간단한 다이나믹 프로그래밍 풀이

import collections
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.defaultdict(int)
        for num in nums:
            if counts[num] == 0:
                counts[num] = nums.count(num)

            if counts[num] > len(nums) // 2:
                return num


# In[8]:


#풀이3
#재귀 풀이의 특성상 다이나믹 프로그래밍이나 다른 방시겡 비해서는 속도가 다소 느린 편

#분할 정복
#병합 정렬과 매우 유사한 방식으로 풀이할 수 있음
#쪼갠 다음 정렬해서 각각의 엘리먼트를 전부 리턴하는 병합 정렬과 달리 
#과반수 후보군에 해당하는 엘리먼트만 리턴하면서 계속 백트래킹하면 최종적으로 정답이 남게 됨
import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #끊어서 리턴
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2
        
        #분할 시도
        #a와b는 각각 최소 단위로 쪼개질 것
        #최소단위로 쪼개질 때 해당하는 값 리턴하게 될 것
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])
        
        #백트래킹될 때 처리하는 부분(정복에 해당하는 부분)
        #a가 만약 현재 분할된 리스트 nums에서 과반수를 차지한다면 해당 인덱스는 1
        #=> [b,a][1]이 되어 a 리턴할 것. 이외에는 b리턴
        return [b, a][nums.count(a) > half]


# In[10]:


Solution().majorityElement(nums_1)


# In[11]:


Solution().majorityElement(nums_2)


# In[ ]:


#풀이4
#파이썬다운 방식
#매우 직관적이며 쉬운 알고리즘

#정렬하여 가운데를 지정하면 반드시 과반수 이상인 엘리먼트일 것
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]

