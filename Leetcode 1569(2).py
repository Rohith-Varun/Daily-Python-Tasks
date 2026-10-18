from typing import List

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Precompute combinations using Pascal's triangle
        comb = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            comb[i][0] = 1
            for j in range(1, i + 1):
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD

        def get_ways(arr: List[int]) -> int:
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            # Use generator expressions/list comps efficiently or pass indices, 
            # but here's a faster flat separation:
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x >= root] # BST handles duplicates or values safely
            
            L = len(left)
            R = len(right)
            
            ways_comb = comb[L + R][L]
            ways_left = get_ways(left) if L > 0 else 1
            ways_right = get_ways(right) if R > 0 else 1
            
            return (ways_comb * ways_left * ways_right) % MOD

        return (get_ways(nums) - 1) % MOD
