#!/usr/bin/env python
# coding: utf-8

# In[1]:


#숫자와 연산자를 입력받아 (괄호를 삽입하여) 가능한 모든 조합의 결과를 출력하라


# In[2]:


input_1 = '2-1-1'
input_2 = '2*3-4*5'


# In[7]:


#append() vs extend()
#리스트에 또 다른 리스트를 삽입할 때 'append()'는 리스트 전체를 또 다른 엘리먼트로 처리(리스트 전체가 하나의 원소로 추가됨)
#'extend()' : 삽입 대상의 리스트를 풀어서 각각의 엘리먼트로 확장해 삽입


# In[8]:


#풀이
#분할 정복을 이용한 다양한 조합
#*, -, + 연산자가 등장할 때 좌/우 분할을 하고 각각 계산 결과 리턴

from typing import List

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        
        #연산자를 기준으로 재귀로 left, right를 계속 분할하고, 분할된 값은 compute()함수로 계산할 결과를 extend()로 확장
        #계산하는 부분
        #각각 반복으로 단수형 값을 추출해 계산
        #가독성을 좀 더 높이기 위해 풀어서 작성
        #eval() : 문자열을 파싱하고 파이썬 표현식으로 처리해주는 역할
        #ex) eval('4+5') => 9
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r)))
            return results
        
        #분할 결과를 리턴받으려면 input이 숫자형일 때 리턴하게 함
        #=> 분할의 결과가 최종적으로 숫자형인 타입을 재귀의 최종 결과로 리턴하게 될 것
        if input.isdigit():
            return [int(input)]

        results = []
        for index, value in enumerate(input):
            if value in "-+*":
                left = self.diffWaysToCompute(input[:index])
                right = self.diffWaysToCompute(input[index + 1:])

                results.extend(compute(left, right, value))
        return results


# In[9]:


Solution().diffWaysToCompute(input_1)


# In[10]:


Solution().diffWaysToCompute(input_2)

