#!/usr/bin/env python
# coding: utf-8

# 주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다

# In[40]:


#내 풀이
def isPalindrome(s):
    strs = []
    for c in s:
        if c.isalnum():
            strs.append(c.lower())
    
    l = int(len(strs) / 2)
    for i in range(l+1):
        z = len(strs) - i - 1
        true = 0
        false = 0
        if s[i] == s[z]:
            true += 1
        else:
            false += 1
    
    if false != 0:
        return("False")
    else:
        return("True")


# In[2]:


#풀이1
def isPalindrome(self, s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
            
    #길이가 0이 될 때까지 반복
    #첫 번째 시행 후 pop()에 의해 처음과 마지막 문자 삭제된 문자열로 실행
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
        
    return True


# In[4]:


#풀이2
from collections import deque

def isPalindrome(self, s: str) -> bool:
    #자료형 데크로 선언
    strs : Deque = collections.deque()
        
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    
    #pop(0)는 O(n), 데크의 popleft()는 O(1)
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    
    return True


# In[8]:


#풀이3
import re
def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    
    #정규식으로 불필요한 문자 필터링
    #[^a-z0-9] : 영숫자를 제외한 나머지 문자
    #불필요한 문자들을 공백으로 
    s = re.sub('[^a-z0-9]', '', s)
    
    #s[::-1] : s의 배열을 뒤집은 문자열
    return s == s[::-1]


# In[41]:


s = "A man, a plan, a canal: Panama"


# In[42]:


isPalindrome(s)


# In[28]:


s = "race a car"


# In[29]:


isPalindrome(s)

