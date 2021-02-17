#!/usr/bin/env python
# coding: utf-8

# In[1]:


#A에서 Z로 표현된 태스크가 있다. 각 간격마다 CPU는 한 번의 태스크만 실행할 수 있고, n번의 간격 내에는 동일한 태스크를 실행할 수 업승ㅁ
#더 이상 태스크를 실행할 수 없는 경우 아이들(idle) 상태가 됨. 모든 태스크를 실행하기 위한 최소 간격을 출력하라


# In[4]:


tasks = ['A', 'A', 'A', 'B', 'B', 'B']
n = 2


# In[5]:


#풀이
#우선순위 큐 이용
#아이템 추출한 이후에는 매번 아이템 개수를 업데이트해줘야 함
#heapq만으로 구현하기에는 상당히 번거로운 작업들이 필요하기 때문에 가능한 파이썬답게 간결한 방식으로 풀기 위해 Counter 모듈 사용

import collections
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0

        while True:
            sub_count = 0
            # 개수 순 추출
            #Counter모듈은 개수를 줄이는 메소드도 지원
            #n 대신 n+1를 사용하여 별도의 예외 처리 필요 없음
            for task, _ in counter.most_common(n + 1): #최대 힙과 같은 역할
                sub_count += 1
                result += 1

                counter.subtract(task) #1개씩 개수를 별도로 줄여나가기
                
                #Counter는 0과 음수도 처리하는 특징이 있기 때문에 매번 0이하인지 체크 or 0이하일 때 아예 삭제
                #0 이하인 아이템을 목록에서 완전히 제거(실무에서라면 코드만 작성해두면 무슨 역할을 하는지 아무도 모르기 때문에 간단한 주석 붙여줌)
                #빈 collection.Counter()를 더하는 것으로, 0이하인 아이템을 목록에서 아예 제거해버림
                #매우 유용한 Hack
                counter += collections.Counter()

            if not counter:
                break

            result += n - sub_count + 1

        return result


# In[7]:


Solution().leastInterval(tasks, n)

