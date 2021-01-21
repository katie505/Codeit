#!/usr/bin/env python
# coding: utf-8

# In[1]:


#그래프 노드 구현


# In[2]:


class StationNode:
    """지하철 역 노드를 나타내는 클래스"""
    def __init__(self, name, num_exits):
        self.name = name
        self.num_exits = num_exits #지하철 출구 개수


# In[3]:


#지하철 역 노드 인스턴스 생성
station_0 = StationNode("교대역", 14)
station_1 = StationNode("사당역", 14)
station_2 = StationNode("종로3가역", 16)
station_3 = StationNode("서울역", 16)


# In[5]:


#노드들을 파이썬 리스트에 저장
#그래프에서는 노드들의 특정 고유값을 이용해서 접근할 수 있음
#각 노드 인스턴스들을 배열이나 파이썬 리스트에 저장했기 때문에 원하는 지하철 역 노드에 효율적으로 접근할 수 있음
stations = [station_0, station_1, station_2, station_3]

#노드들을 해시 테이블(파이썬 딕셔너리)에 저장
#좀 더 직관적으로 접근할 수 있음
#해시 테이블에서 키는 한 유저가 고유로 갖는 값으로 해야함
stations = {
    "교대역" : station_0,
    "사당역" : station_1,
    "종로3가역" : station_2,
    "서울역" : station_3
}

