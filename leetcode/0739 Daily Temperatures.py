#!/usr/bin/env python
# coding: utf-8

# In[1]:


#매일의 화씨온도 리스트 T를 입력받아서, 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지를 출력하라


# In[2]:


T = [73, 74, 75, 71, 69, 72, 76, 73]


# In[3]:


#풀이
from typing import List

class Solution():
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        #디폴트는 0. 더 높은 온도가 나오지 않아 스택이 비워지지 않았다면
        #해당 인덱스는 해당 없음. 즉, 0으로 남게 됨
        answer = [0] * len(T)
        stack = []
        
        for i, cur in enumerate(T):
            #현재 온도가 스택 맨 위에 해당하는 온도보다 높다면 
            #스택을 pop()하여 삽입한 인덱스와 온도 반환
            #answer에 현재 인덱스와 스택에 쌓아둔 인덱스의 차이
            #며칠을 기다려야 더 따뜻한 날이 오는지 알 수 있음
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
            
        return answer


# In[4]:


Solution().dailyTemperatures(T)

