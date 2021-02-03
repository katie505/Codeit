#!/usr/bin/env python
# coding: utf-8

# In[1]:


#m*n 행렬에서 값을 찾아내는 효율적인 알고리즘을 구현하라
#행렬은 왼쪽에서 오른쪽, 위에서 아래 오름차순으로 정렬되어 있다
#이 문제는 이진 검색으로 풀이가 어려움


# In[13]:


matrix = [
    [1,4,7,11,15],
    [2,5,8,12,19],
    [3,6,9,16,22],
    [10,13,14,17,24],
    [18,21,23,26,30]
]
target1 = 5
target2 = 20


# In[14]:


#풀이1
#첫 행의 맨 뒤 요소를 택한 다음, 타겟이 이보다 작으면 왼쪽으로, 크면 아래로 이동하게 하는 방법
class Solution:
    def searchMatrix(self, matrix, target):
        # 예외 처리
        if not matrix:
            return False

        # 첫 행의 맨 뒤
        row = 0
        col = len(matrix[0]) - 1

        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True
            # 타겟이 작으면 왼쪽으로
            elif target < matrix[row][col]:
                col -= 1
            # 타겟이 크면 아래로
            elif target > matrix[row][col]:
                row += 1
        return False


# In[15]:


#풀이2
#파이썬다운 방식
#내부적으로 행렬에 값이 존재하는지 여부를 위에서부터 차례대로 한 줄씩 탐색

class Solution:
    def searchMatrix(self, matrix, target):
        return any(target in row for row in matrix)


# In[16]:


Solution().searchMatrix(matrix, target1)


# In[17]:


Solution().searchMatrix(matrix, target2)

