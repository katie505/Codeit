#!/usr/bin/env python
# coding: utf-8

# In[1]:


#중복된 문자를 제외하고 사전식 순서로 나열하라
#사전식 순서 : 사전에서 가장 먼저 찾을 수 있는 순서


# In[4]:


#풀이1 재귀를 이용한 분리

from typing import List

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        #문자열이 들어오면 먼저 중복을 제거하고 알파벳 순으로 정렬
        #집합 : 중복된 문자가 제거된 자료형
        #중복이 제거하지 않은 기존의 문자열에서 찾아 해당 문자부터 끝까지 접미사로 빼낸다
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            
            #전체 집합과 접미사 집합이 일치할때 분리 진행
            #suffix의 맨 첫번째 문자를 반환시키고 그 문자를 모두 없애버린(replace() 이용)호출해서 정답 얻기
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''


# In[7]:


Solution().removeDuplicateLetters('bcabc')


# In[8]:


Solution().removeDuplicateLetters("cbacdcbc")


# In[9]:


Solution().removeDuplicateLetters("ebcabc")


# In[10]:


Solution().removeDuplicateLetters("ebcabce")


# In[15]:


import collections
from typing import List

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, stack = collections.Counter(s), []
        
        #현재 문자 char가 스택에 쌓여 있는 문자이고, 뒤에 다시 붙일 문자가 남아 있다면 쌓아둔 걸 꺼내서 없앤다
        for char in s:
            counter[char] -= 1
            if char in stack:
                continue
            
            #for문의 char의 문자와 stack에 있는 가장 최근 문자 stack[-1]을 비교하여 stack[-1]이 더 사전순에서 뒤쪽 문자열이라면 잘못되었기 때문에 stack[-1] 제거
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                stack.pop()
            
            #아닐 경우 계속 스택에 쌓아 출력
            stack.append(char)

        return ''.join(stack)


# In[16]:


Solution().removeDuplicateLetters("ebcabc")


# In[17]:


Solution().removeDuplicateLetters('bcabc')


# In[18]:


Solution().removeDuplicateLetters("cbacdcbc")


# In[19]:


Solution().removeDuplicateLetters("ebcabce")

