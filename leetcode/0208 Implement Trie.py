#!/usr/bin/env python
# coding: utf-8

# In[1]:


#트라이의 insert, search, startsWith 메소드 구현하라


# In[4]:


#풀이
#딕셔너리를 이용해 간결한 트라이 구현

import collections

class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    #self.children을 defaultdict()로 선언한다면 insert() 메소드에서 매번 if로 체크하는 구문 없앨 수 있음
    # 단어 삽입
    # 삽입 시 루트부터 자식 노드가 점점 깊어지면서 문자 단위의 다진 트리형태가 됨
    # 각각의 노드는 word 값을 갖는다
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True

    # 단어 존재 여부 판별
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.word

    # 문자열로 시작 단어 존재 여부 판별
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True


# In[6]:


trie = Trie()
trie.insert('apple')
trie.search('apple')


# In[7]:


trie.search('app')


# In[8]:


trie.startsWith('app')


# In[9]:


trie.insert('app')


# In[10]:


trie.search('app')

