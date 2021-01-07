#!/usr/bin/env python
# coding: utf-8

# In[1]:


#덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라
#코딩 인터뷰 시 높은 빈도로 출제되는 문제


# In[ ]:


#이 문제는 파이썬에서도 아무런 문제가 없었지만 어떤 문제들을 언어별로 타임아웃이 발생하는 경우도 있음
#언어의 선택은 실행 속도에 매우 중요한 영향을 미치며, 일부 코딩 테스트 플랫폼에서는 동일한 알고리즘인데
#언어에 따라 타임아웃이 발생하는 경우가 있다
#파이썬 풀이에서 계속 타임아웃이 발생하고 그 원인을 찾기 어렵다면, 동일한 알고리즘을 다른 언어로 재작성해
#성능을 확인해볼 필요가 있다.


# In[3]:


nums = [2, 7, 11, 15]
target = 9


# In[6]:


#내 풀이
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                return[i, j]


# In[10]:


#풀이1
#부르트 포스 : 배열을 2번 반복하면서 모든 조합을 더해서 일일이 확인해보는 무차별 대입 방식
from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return[i, j]


# In[11]:


#풀이2
#모든 조합을 비교하지 않고 정답, 즉 타겟에서 첫 번째 값을 뺀 값 target - n이 존재하는지 탐색

from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        complement = target - n
        
        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]


# In[15]:


#풀이3

from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    
    #키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i
        
    #타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return[i, nums_map[target - num]]


# In[17]:


#풀이4

from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    nums_map = {}
    
    #하나의 for문으로 통합
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return[nums_map[target - num], i]
        nums_map[num] = i


# In[20]:


#풀이5(좋지X)
#이 문제는 투 포인터로 풀 수 없음. 입력값인 nums는 정렬된 상태가 아니고, 
#정렬하면 인덱스가 모두 엉망이 됨. 
#인덱스를 찾아내는 문제에서 정렬을 통해 인덱스를 섞어 버리면 안됨 => 원래 인덱스를 찾을 수가 없기 때문
from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1
    
    while not left == right:
        #합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
        if nums[left] + nums[right] < target:
            left += 1
        
        #합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return[left, right]


# In[ ]:


#풀이6
#고(Go)언어 : C언어 개발에 참여했던 사람들이 구글에서 개발한 오픈소스 객체지향언어


# In[21]:


twoSum(nums, target)

