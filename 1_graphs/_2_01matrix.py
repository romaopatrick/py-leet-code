#2. 01 Matrix: https://leetcode.com/problems/01-matrix/description/
import collections

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        
        rows, cols = len(mat), len(mat[0])
        
        dict = [[float('inf')] * cols for _ in range(rows)]
        
        q = collections.deque()
        
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dict[r][c] = 0
                    q.append((r, c))
        
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
                    
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                rr, cc = dr + r, dc + c
                
                if 0 <= rr < rows and 0 <= cc < cols:
                    if dict[rr][cc] > dict[r][c] + 1:
                        dict[rr][cc] = dict[r][c] + 1
                        q.append((rr, cc))
                        
        return dict