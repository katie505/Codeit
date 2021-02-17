#!/usr/bin/env python
# coding: utf-8

# In[1]:


#대문자로 구성된 문자열s가 주어졌을 때 k번만큼의 변경으로 만들 수 있는, 연속으로 반복된 문자열의 가장 긴 길이를 출력하라


# In[ ]:


#가독성과 실행속도는 반비례인 관계가 종종 있음


# In[2]:


s = 'AAABBC'
k = 2


# In[3]:


#풀이
#투포인터, 슬라이딩 윈도우, Counter 모두 이용
#슬라이딩 윈도우(오른쪽 포인터가 계속 우측으로 이동)
#투 포인터(왼쪽 포인터를 계속 좁혀서 범위를 조절해 나감)
#오른쪽 포인터에서 왼쪽 포인터 위치를 뺀 다음, 윈도우 내 출현 빈도가 가장 높은 문자의 수를 뺀 값이 k와 같을 수 있는 수 중 가장 큰 최댓값

import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        counts = collections.Counter()
        for right in range(1, len(s) + 1):
            counts[s[right - 1]] += 1
            # 가장 흔하게 등장하는 문자 탐색
            max_char_n = counts.most_common(1)[0][1]

            # k 초과시 왼쪽 포인터 이동
            if right - left - max_char_n > k:
                counts[s[left]] -= 1
                left += 1
        return right - left


# In[4]:


Solution().characterReplacement(s, k)

