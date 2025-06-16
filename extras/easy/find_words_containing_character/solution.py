class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        counter = []
        
        for i in range(len(words)):
            count = words[i].count(x)
            if count > 0:
                counter.append(i)

        return counter