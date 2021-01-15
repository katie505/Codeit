#!/usr/bin/env python
# coding: utf-8

# In[2]:


#스택을 이용해 다음 연산을 지원하는 큐를 구현하라
#- push(x) : 요소x를 큐 마지막에 삽입
#- pop() : 큐 처음에 있는 요소 제거
#- peek() : 큐 처음에 있는 요소 조회
#- empty() : 큐가 비어 있는지 여부 리턴


# In[3]:


class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []
        
    def push(self, x):
        self.input.append(x)
        
    def pop(self):
        self.peek()
        return self.output.pop()
    
    def peek(self):
        #output이 없으면 모두 재입력
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
    
    def empty(self):
        return self.input == [] and self.output == []


# In[4]:


queue = MyQueue()
queue.push(1)
queue.push(2)


# In[5]:


queue.peek()


# In[6]:


queue.pop()


# In[7]:


queue.empty()

