# https://leetcode.com/problems/implement-trie-prefix-tree/
class Trie:
    def __init__(self):
        self.tree: list[str] = []

    def insert(self, word: str) -> None:
        self._insert_next(word, len(self.tree) // 2)

    def _insert_next(self, word, i):
        if len(self.tree) == 0 or i > len(self.tree) - 1:
            self.tree.append(word)
            return
            
        if word == self.tree[i]:
            return
        
        if word < self.tree[i]:
            if i == 0:
                self.tree.insert(0, word)
                return

            if word > self.tree[i - 1]:
                self.tree.insert(i, word)
                return

            self._insert_next(word, i - 1)
            return

        if word > self.tree[i]:
            if i == len(self.tree) - 1:
                self.tree.append(word)
                return

            if word < self.tree[i + 1]:
                self.tree.insert(i, word)
                return

            self._insert_next(word, i + 1)

        return

    def search(self, word: str) -> bool:
        return self._search_next(word, len(self.tree) // 2)

    def _search_next(self, word: str, i: int) -> bool:
        if i > len(self.tree) - 1 or i < 0:
            return False

        node = self.tree[i]
        if node == word:
            return True

        if word < node:
            if i <= 0 or word > self.tree[i-1]:
                return False
            
            return self._search_next(word, i - 1)
        

        if i >= len(self.tree) - 1 or i == 0:
            return False

        return self._search_next(word, i + 1)

    def startsWith(self, prefix: str) -> bool:
        return self._starts_with_recursive(prefix, len(self.tree) // 2)

    def _starts_with_recursive(self, pfx: str, i: int) -> bool:
        if i > len(self.tree) - 1 or i < 0:
            return False

        node = self.tree[i]
        if node.startswith(pfx):
            return True

        if pfx < node:
            if i <= 0 or pfx > self.tree[i-1]:
                return False
            
            return self._starts_with_recursive(pfx, i - 1)
        

        if i >= len(self.tree) - 1 or i == 0:
            return False

        return self._starts_with_recursive(pfx, i + 1)
