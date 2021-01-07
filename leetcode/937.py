#!/usr/bin/env python
# coding: utf-8

# In[1]:


#로그 파일 재정렬
#풀이
from typing import List

def reorderLogFiles(logs: List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    
    #식별자를 제외한 문자열 [1:]을 키로, 후순위로 식별자[0] 지정 정렬
    letters.sort(key = lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits


# In[2]:


logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]


# In[3]:


reorderLogFiles(logs)

