#!/usr/bin/env python
# coding: utf-8

# In[1]:


#가장 긴 팰린드롬 부분 문자열을 출력하라


# In[3]:

#풀이

#다이나믹 프로그래밍보다 좀 더 직관적이면서도 훨씬 더 성능이 좋은
#투 포인터가 중앙을 중심으로 확장한느 형태로 풀이
def longestPalindrome(s: str) -> str:
    #팰린드롬 판별 및 투 포인터 확장
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]
    
    #해당 사항이 없을 때 빠르게 리턴(예외 처리)
    #단어 자체가 팰린드롬
    if len(s) < 2 or s == s[::-1]:
        return s
    
    result = ''
    #슬라이딩 윈도우 우측으로 이동
    for i in range(len(s) - 1):
        result = max(result, 
                        expand(i, i+1), 
                        expand(i, i+2),
                        key = len)
    return result

