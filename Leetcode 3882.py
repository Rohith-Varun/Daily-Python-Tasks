
class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # dp[j] stores all possible XOR values for the current row
        # at column j.
        dp = [0] * n

        for i in range(m):
            for j in range(n):
                val = grid[i][j]

                if i == 0 and j == 0:
                    dp[j] = 1 << val
                else:
                    # Paths can come from above or from the left.
                    prev = dp[j]

                    if j > 0:
                        prev |= dp[j - 1]

                    # XOR the current cell value with every possible
                    # XOR value from the previous paths.
                    dp[j] = 0

                    while prev:
                        bit = prev & -prev
                        prev -= bit

                        xor_value = bit.bit_length() - 1
                        dp[j] |= 1 << (xor_value ^ val)

        # Find the smallest possible XOR value at the bottom-right.
        return (dp[-1] & -dp[-1]).bit_length() - 1
