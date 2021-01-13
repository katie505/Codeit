#!/usr/bin/env python
# coding: utf-8

# In[4]:


#리스트
trending = []

#특정 위치에 데이터 삽입
trending.insert(0, "연예인 A씨")
trending.insert(1, '잠실 콘서트')
trending.insert(2, '한국 휴일 수')
trending.insert(3, '추석 음식')
print(trending)

#괄호를 이용한 인덱스 접근
print(trending[0])
print(trending[1])

trending[2] = 4

print(trending)

#in을 이용한 탐색
print('연예인 A씨' in trending)
print('연예인 B씨' in trending)

#del을 이용한 삭제
del trending[0]

print(trending)


# In[7]:


#데크
from collections import deque

queue = deque()

#큐의 맨 끝에 데이터 삽입
queue.append('상혁')
queue.append('진성')
queue.append('우찬')
queue.append('창동')
queue.append('민석')

print(queue)

#큐의 가장 앞 데이터에 접근
print(queue[0])

#큐 맨 앞 데이터 삭제
#popleft()메소드는 맨 앞 데이터를 삭제하기도 하지만 삭제하는 데이터를 리턴하기도 함
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())
print(queue)


# In[10]:


#데크를 이용해서 스택 구현
from collections import deque

stack = deque()

#스택 맨 끝에 데이터 추가
stack.append('S')
stack.append('K')
stack.append('T')
stack.append('T')
stack.append('1')

print(stack)

#맨 끝 데이터 접근
print(stack[-1])

#맨 끝 데이터 삭제
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack)


# In[15]:


#딕셔너리
grades = {}

#key - value 데이터 삽입
grades['상혁'] = 80
grades['진성'] = 60
grades['우찬'] = 90
grades['창동'] = 70
grades['민석'] = 96
print(grades)

#한 key에 여러 value 저장 시도
grades['진성'] = 100
print(grades)

#key를 이용해서 value 탐색
print(grades['민석'])
print(grades['창동'])

#key를 이용한 삭제
grades.pop('진성')
grades.pop('상혁')
print(grades)


# In[19]:


#세트
finished_classes = set()

#데이터 저장
finished_classes.add('자료 구조')
finished_classes.add('알고리즘')
finished_classes.add('프로그래밍 기초')
finished_classes.add('인터렉티브 웹')
finished_classes.add('데이터 사이언스')

print(finished_classes)

#데이터 탐색
print('컴퓨터 개론' in finished_classes)
print('자료 구조' in finished_classes)

#데이터 삭제
finished_classes.remove('자료 구조')
finished_classes.remove('알고리즘')

print(finished_classes)

