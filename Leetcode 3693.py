class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [0] * (n + 1)
        for j in range(1, n + 1):
            min_cost = float('inf')
            # Check previous steps j-1, j-2, j-3 if they exist (>= 0)
            for k in range(1, 4):
                i = j - k
                if i >= 0:
                    cost = dp[i] + costs[j - 1] + (j - i) ** 2
                    if cost < min_cost:
                        min_cost = cost
            dp[j] = min_cost
            
        return dp[n]
