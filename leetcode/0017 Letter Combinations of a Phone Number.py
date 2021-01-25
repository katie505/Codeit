#!/usr/bin/env python
# coding: utf-8

# In[1]:


#2에서 9까지 숫자가 주어졌을 때 전화번호로 조합 가능한 모든 문자를 출력하라


# In[2]:


#풀이1
#전체를 탐색하여 풀이
#가능한 경우의 수를 모두 조합하는 형태로 전체를 탐색한 후 백트래킹하면서 결과 조합
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            # 입력값을 자릿수로 쪼개어 반복하고, 숫자에 해당하는 모든 문자열을 반복하면서 마찬가지로 문자 단위로 재귀 탐색
            # 끝까지 탐색하면 백트래킹
            if len(path) == len(digits):
                result.append(path)
                return

            # 입력값 자릿수 단위 반복
            for i in range(index, len(digits)):
                # 숫자에 해당하는 모든 문자열 반복
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)

        # 예외 처리
        if not digits:
            return []

        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
               "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        dfs(0, "")

        return result


# In[10]:


#풀이2
#itertools 사용
import itertools

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: # 빈 문자열 예외처리
            return []
        
        diaglos = {
            "1" : "",
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        } # 전화번호 패드

        iterators = [ diaglos[digit] for digit in digits ] # 번호에 맞게 문자 목록 생성
        return [ ''.join(comb) for comb in itertools.product(*iterators) ] # 카테시안 곱


# In[11]:


digits = '23'


# In[12]:


Solution().letterCombinations(digits)

