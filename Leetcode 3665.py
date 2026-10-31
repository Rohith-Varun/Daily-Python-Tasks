from typing import List
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])      
        def get_next(r: int, c: int, d: int):
            while 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                if d == 0:
                    r += 1
                    d = 1
                else:
                    c += 1
                    d = 0
            if not (0 <= r < m and 0 <= c < n):
                return None
            return (r, c, d)
        dp = [[[0, 0] for _ in range(n)] for _ in range(m)]       
        res_right = get_next(0, 1, 0)
        if res_right:
            r, c, d = res_right
            dp[r][c][d] = (dp[r][c][d] + 1) % MOD        
        res_down = get_next(1, 0, 1)
        if res_down:
            r, c, d = res_down
            dp[r][c][d] = (dp[r][c][d] + 1) % MOD
        for i in range(m):
            for j in range(n):
                for d in range(2):
                    ways = dp[i][j][d]
                    if ways == 0:
                        continue
                    if i == 0 and j == 0:
                        continue                   
                    nxt = get_next(i, j + 1, 0)
                    if nxt:
                        ni, nj, nd = nxt
                        dp[ni][nj][nd] = (dp[ni][nj][nd] + ways) % MOD                      
                    nxt = get_next(i + 1, j, 1)
                    if nxt:
                        ni, nj, nd = nxt
                        dp[ni][nj][nd] = (dp[ni][nj][nd] + ways) % MOD
        return (dp[m - 1][n - 1][0] + dp[m - 1][n - 1][1]) % MOD
