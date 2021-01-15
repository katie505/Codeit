#!/usr/bin/env python
# coding: utf-8

# In[2]:


#큐를 이용해 다음 연산을 지원하는 스택을 구현하라
#- push(x) : 요소 x를 스택에 삽입
#- pop() : 스택의 첫 번째 요소 삭제
#- top() : 스택의 첫 번째 요소 추출
#- empty() : 스택이 비어 있는지 여부 리턴


# In[3]:


import collections

class Mystack:
    def __init__(self):
        self.q = collections.deque()
        
    def push(self, x):
        self.q.append(x)
        #큐에서 맨 앞 요소를 끄집어낼 때 스택처럼 가장 먼저 삽입한 요소가 나오게 될 것
        #요소 삽입 후 맨 앞에 두는 상태로 재정렬
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
    
    def pop(self):
        return self.q.popleft()
    
    def top(self):
        return self.q[0]
    
    def empty(self):
        return len(self.q) == 0


# In[8]:


stack = Mystack()
stack.push(1)
stack.push(2)


# In[9]:


stack.top()


# In[10]:


stack.pop()


# In[11]:


stack.empty()

