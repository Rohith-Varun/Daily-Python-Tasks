class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n    
        max_len = 1
        inc_len = 1
        dec_len = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                inc_len += 1
                dec_len = 1
            elif nums[i] < nums[i - 1]:
                dec_len += 1
                inc_len = 1
            else:
                inc_len = 1
                dec_len = 1
            if inc_len > max_len:
                max_len = inc_len
            if dec_len > max_len:
                max_len = dec_len
                
        return max_len
