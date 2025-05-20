from typing import Optional


class TrieNode:
    def __init__(self):
        self.children: list[Optional[TrieNode]] = [None] * 26
        self.word_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.word_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if node.children[idx] is None:
                return False
            node = node.children[idx]
        return node.word_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            idx = ord(char) - ord('a')
            if node.children[idx] is None:
                return False
            node = node.children[idx]
        return True
