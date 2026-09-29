class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if (m + n) % 2 == 0 or grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(1)

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue
                
                delta = 1 if grid[r][c] == '(' else -1
                
                # Transition from top cell
                if r > 0:
                    for b in dp[r - 1][c]:
                        if b + delta >= 0:
                            dp[r][c].add(b + delta)
                            
                # Transition from left cell
                if c > 0:
                    for b in dp[r][c - 1]:
                        if b + delta >= 0:
                            dp[r][c].add(b + delta)

        return 0 in dp[m - 1][n - 1]
