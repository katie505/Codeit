#!/usr/bin/env python
# coding: utf-8

# In[1]:


#단어 리스트에서 words[i]+words[j]가 팰린드롬이 되는 모든 인덱스 조합(i, j)를 구하라


# In[2]:


words1 = ['abcd', 'dcba', 'lls', 's', 'sssll']
words2 = ['bat', 'tab', 'cat']


# In[3]:


#풀이1
#팰린드롬을 브루트 포스로 계산
#각각의 모든 조합을 구성해보고 이 구성이 팰린드롬인지 여부 판별
#리트코드에서는 타임아웃이 발생하며 테스트 케이스를 통과할 수 없음 = O(n^2)

from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(word):
            return word == word[::-1]

        output = []
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i == j:
                    continue
                if is_palindrome(word1 + word2):
                    output.append([i, j])
        return output


# In[4]:


#풀이2
#O(n)
#팰린드롬으로 판별할 수 있는 경우
#1. 끝까지 탐색했을 때 word_id가 있는 경우
#2. 끝까지 탐색했을 때 palindrome_word_ids가 있는 경우
#3. 탐색 중간에 word_id가 있고 나머지 문자가 팰린드롬인 경우
import collections
from typing import List


# 트라이 저장할 노드
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_word_ids = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word[::] == word[::-1]

    # 단어 삽입
    def insert(self, index, word) -> None:
        node = self.root
        #뒤집은 다음, 문자 단위로 계속 내려가면서 트라이를 구현하고, 
        #각각의 단어가 끝나는 지점에는 단어 인덱스를 word_id = index
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[0:len(word) - i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
        node.word_id = index
    
    #단어를 뒤집어서 구축한 트라이이기 때문에 입력값은 순서대로 탐색하다가, 끝나는 지점의 word_id 값이 -1이 아니라면,
    #현재 인덱스 index와 해당 word_id는 팰린드롬으로 판단할 수 있음
    def search(self, index, word) -> List[List[int]]:
        result = []
        node = self.root

        while word:
            # 판별 로직 3) (본문 설명 참고)
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]

        # 판별 로직 1) (본문 설명 참고)
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])

        # 판별 로직 2) (본문 설명 참고)
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])

        return result


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert(i, word)

        results = []
        for i, word in enumerate(words):
            results.extend(trie.search(i, word))

        return results


# In[5]:


Solution().palindromePairs(words1)


# In[6]:


Solution().palindromePairs(words2)

