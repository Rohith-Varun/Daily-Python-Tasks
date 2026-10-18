import math
from typing import List

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Precompute combinations (Pascal's Triangle) for O(1) lookups
        # comb[n][k] = n choose k mod MOD
        comb = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            comb[i][0] = 1
            for j in range(1, i + 1):
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD

        def get_ways(arr: List[int]) -> int:
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = []
            right = []
            
            # Single pass to partition elements while preserving relative order
            for x in arr[1:]:
                if x < root:
                    left.append(x)
                else:
                    right.append(x)
            
            L = len(left)
            R = len(right)
            
            # O(1) combination lookup using precomputed table
            ways_comb = comb[L + R][L]
            
            ways_left = get_ways(left)
            ways_right = get_ways(right)
            
            return (ways_comb * ways_left * ways_right) % MOD

        return (get_ways(nums) - 1) % MOD
