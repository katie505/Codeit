#!/usr/bin/env python
# coding: utf-8

# In[1]:


#원형으로 경로가 연결된 주유소 목록
#각 주유소는 gas[i]만큼의 기름을 갖고 있으며, 다음 주유소를 이동하는데 cost[i]가 필요함
#기름이 부족하면 이동할 수 없다고 할 때 모든 주유소를 방문할 수 있는 출발점의 인덱스 출력하라
#출발점이 존재하지 않을 경우 -1을 리턴하며, 출발점은 유일함


# In[2]:


gas = [1,2,3,4,5]
cost = [3,4,5,1,2]


# In[7]:


#풀이1
#처음부터 한 칸씩 출발점으로 지정하고, 나머지 모든 주유소를 방문하는 방법으로 풀이
#주유소의 경로는 원형으로 연결되어 있으므로, 모듈로 연산(나머지 연산)을 하여 인덱스를 다시 0부터 지정할 수 있게 함
#그리고 모든 주유소를 방문 가능한지 점검
#가능할 경우 출발점이 유일하다는 제약이 있기 때문에, 바로 해당 출발점을 결과로 리턴
#만약 중간에 끊길 경우 다시 다음번 출발점으로 반복

#두 번의 루프가 중첩되어 있으므로 O(n^2). 겨우 풀리는 수준
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for start in range(len(gas)):
            fuel = 0
            for i in range(start, len(gas) + start):
                index = i % len(gas)

                can_travel = True
                if gas[index] + fuel < cost[index]:
                    can_travel = False
                    break
                else:
                    fuel += gas[index] - cost[index]
            if can_travel:
                return start
        return -1


# In[4]:


Solution().canCompleteCircuit(gas, cost)


# In[5]:


#풀이2
#전체 기름의 양이 전체 비용보다 클 경우 반드시 전체를 방문할 수 있는 출발점 존재
#비용이 더 클 때 리턴해버리면, 이제 반드시 존재하는 경우만 남아 있게 됨
#따라서 전체를 방문하면서 성립되지 않는 경우는 출발점을 한 칸씩 뒤로 밀어냄
#성립되지 않는 지점이 있다면 그 앞은 전부 출발점이 될 수 ㅇ벗음

#수학에서 귀류법으로 증명하는 것과 유사
#모순을 이끌어내 거짓인 경우를 제외하면, 가능한 지점은 제외하지 못한 지점이고, 자연스럽게 남은 곳이 정답이 됨

#한 번의 루프
#전체 sum()을 비교하는 구문을 통과했다면 반드시 출발점이 존쟇나ㅡㄴ 경우

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 모든 주유소 방문 가능 여부 판별
        if sum(gas) < sum(cost):
            return -1

        start, fuel = 0, 0
        for i in range(len(gas)):
            # 출발점이 안되는 지점 판별
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
        return start


# In[6]:


Solution().canCompleteCircuit(gas, cost)

