class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []

        def backtrack(start: int):
            if start == len(nums):
                res.append(nums[:])  # Append a copy of the current permutation
                return

            for i in range(start, len(nums)):
                # Swap current index with index i
                nums[start], nums[i] = nums[i], nums[start]
                
                # Recursively explore the next element
                backtrack(start + 1)
                
                # Backtrack: revert the swap
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return res
