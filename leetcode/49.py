#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 문자열 배열을 받아 애너그림 단위로 그룹핑하라


# In[2]:


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


# In[6]:

#풀이
import collections
from typing import List
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)
    #존재하지  키를 삽입하려할 경우 KeyError가 발생하므로, 에러가 나지 않도록 항상 디폴트를
    #생성해주는 defulatdict()선언 => 매번 키 존재 여부를 체크하지 않고 비교구문 생략해 간결하게 구성됨
    
    #sorted()로 문자열 정렬 후 결과를 리스트로 리턴
    #다시 키로 사용하기 위해 join()으로 합쳐 이 값을 키로 하는 딕셔너리로 구성
    #애너그램 관계인 단어들을 정렬하면, 서로 같은 값을 갖게 됨
    #애너그램끼리는 같은 키 값을 갖게 됨
    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    
    return list(anagrams.values())


# In[7]:


groupAnagrams(strs)

