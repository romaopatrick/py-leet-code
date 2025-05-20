class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rotten = 2
        fresh = 1
        none = 0
        impossible = -1
        
        minutes = 0
        
        rows, cols = len(grid), len(grid[0])

        def is_legal(r, c):
            return 0 <= r < rows and 0 <= c < cols

        def dfs(r, c, dfs_grid):
            dsf_minutes = 0
            if not is_legal(r, c) or dfs_grid[r][c] in [rotten, none]:
                return dsf_minutes

            dfs_grid[r][c] = rotten
            dsf_minutes += 1
            dsf_minutes += min(
                dfs(r + 1, c, dfs_grid),
                dfs(r - 1, c, dfs_grid), 
                dfs(r, c + 1, dfs_grid), 
                dfs(r, c - 1, dfs_grid))

            return dsf_minutes

        has_rotten = False
        has_zero_fresh = False
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == rotten and not has_rotten:
                    has_rotten = True
                    continue
                
                if grid[r][c] == fresh:
                    dsf_minutes = dfs(r, c, grid.copy())
                    if dsf_minutes == 0 and not has_zero_fresh:
                        has_zero_fresh = True
                        
                    minutes = max(minutes, dsf_minutes)
        
        if has_rotten and has_zero_fresh:
            return impossible
        
        return minutes
                    
            
            
                    
                    
