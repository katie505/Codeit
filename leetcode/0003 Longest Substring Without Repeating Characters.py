#!/usr/bin/env python
# coding: utf-8

# In[1]:


#중복 문자가 없는 가장 긴 부분 문자열의 길이를 리턴하라


# In[3]:


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            # 이미 등장했던 문자라면 `start` 위치 갱신
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:  # 최대 부분 문자열 길이 갱신
                max_length = max(max_length, index - start + 1)

            # 현재 문자의 위치 삽입
            used[char] = index

        return max_length


# In[4]:


s = 'abcabcbb'
Solution().lengthOfLongestSubstring(s)


# In[5]:


s = 'bbbbb'
Solution().lengthOfLongestSubstring(s)


# In[6]:


s = 'pwwkew'
Solution().lengthOfLongestSubstring(s)

