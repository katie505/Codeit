#!/usr/bin/env python
# coding: utf-8

# In[53]:


# 원형 큐를 디자인하라
# 원형 큐 : FIFO 구조를 지님. 링 버퍼라고도 부름.


# In[62]:


#풀이
class MyCircularQueue:
    # k : 큐의 크기
    #
    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0 # front 포인터
        self.p2 = 0 # rear 포인터

    # enQueue(): rear 포인터 이동
    # 삽입 연산
    def enQueue(self, value: int) -> bool:
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:
            return False

    # deQueue(): front 포인터 이동
    # 삭제 연산
    # 요소를 꺼내지 않고 삭제만 수행
    def deQueue(self) -> bool:
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True

    def Front(self) -> int:
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def Rear(self) -> int:
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]

    def isEmpty(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is not None


# In[63]:


circular = MyCircularQueue(5)


# In[64]:


circular.enQueue(10)


# In[65]:


circular.enQueue(20)


# In[66]:


circular.enQueue(30)


# In[67]:


circular.enQueue(40)


# In[69]:


circular.Rear()


# In[70]:


circular.isFull()


# In[71]:


circular.deQueue()


# In[72]:


circular.deQueue()


# In[73]:


circular.enQueue(50)


# In[74]:


circular.enQueue(60)


# In[75]:


circular.Rear()


# In[76]:


circular.Front()

