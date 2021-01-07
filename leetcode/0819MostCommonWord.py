#!/usr/bin/env python
# coding: utf-8

# In[1]:


#금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다


# In[31]:


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit"
banned = ["hit"]


# In[32]:

#풀이
from typing import List
import collections
import re
def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    #데이터 클렌징 : 입력값에 대한 전처리
    #정규식 이용
    #\w : 단어 문자를 뜻하며, ^은 not을 의미. 즉, 단어가 아닌 모든 문자를 공백으로 치환
    #리스트 컴프리헨션
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split()
                 if word not in banned]
    counts = collections.Counter(words)
    
    #(단어 개수)[인덱스][인덱스]
    #(1) : 가장 흔하게 등장하는 단어의 첫 번째 값 = [('ball', 2)]
    #(1)[0] = ('ball', 2)
    return counts.most_common(1)[0][0]


# In[33]:


mostCommonWord(paragraph, banned)

