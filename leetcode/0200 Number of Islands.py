#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1을 육지로, 0을 물로 가정한 2D 그리드 맵이 주어졌을 때, 섬의 개수를 계산하라
#(연결되어 있는 1의 덩어리 개수를 구하라)


# In[3]:


#풀이
#그래프는 아니지만 사실상 동서남북이 모두 연결된 그래프로 가정하고 동일한 형태로 처리할 수 있으며, 
#'네 방향 각각 DFS 재귀'를 이용해 탐색을 끝마치면 1이 증가하는 형태로 육지의 개수 파악가능
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            # 더 이상 땅이 아닌 경우 종료
            # 행렬 입력값인 grid의 행, 열 단위로 육지(1)인 곳을 찾아 진행하다가 육지를 발견하면
            # self.dfs() 호출해 탐색 시작
            
            # 예외처리
            if i < 0 or i >= len(grid) or \ # 행 예외 처리
                    j < 0 or j >= len(grid[0]) or \ # 열 예외 처리
                    grid[i][j] != '1': # 물 예외 처리
                return #육지가 아닌 곳은 return으로 종료 조건 설정

            grid[i][j] = 0 # 육지 제거
            # 동서남북 탐색
            dfs(i + 1, j) #남
            dfs(i - 1, j) #북
            dfs(i, j + 1) #동
            dfs(i, j - 1) #서
        
        #재귀 호출이 백트래킹으로 모두 빠져 나오면 섬 하나를 발견한 것으로 간주
        #이미 방문한 곳은 1이 아닌 값으로 마킹
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    # 모든 육지 탐색 후 카운트 1 증가
                    count += 1
        return count


# In[4]:


grid = [
    ['1','1','1','1','0'],
    ['1','1','0','1','0'],
    ['1','1','0','0','0'],
    ['0','0','0','0','0']
]


# In[5]:


Solution().numIslands(grid)


# In[6]:


grid = [
    ['1','1','0','0','0'],
    ['1','1','0','0','0'],
    ['0','0','1','0','0'],
    ['0','0','0','1','1']
]


# In[7]:


Solution().numIslands(grid)

