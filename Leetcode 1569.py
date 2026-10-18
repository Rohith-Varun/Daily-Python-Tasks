import math
from typing import List

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        def helper(arr: List[int]) -> int:
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            
            # Combinations: ways to interleave 'left' and 'right' elements
            # math.comb(n, k) computes n choose k efficiently
            ways_comb = math.comb(len(left) + len(right), len(left)) % MOD
            
            # Recursively calculate ways for left and right subtrees
            ways_left = helper(left)
            ways_right = helper(right)
            
            return (ways_comb * ways_left * ways_right) % MOD

        # Subtract 1 because the original given array order itself 
        # shouldn't be counted as a "reordering".
        return (helper(nums) - 1 + MOD) % MOD
