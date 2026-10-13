class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=abs, reverse=True)

        ans = 0
        n = len(nums)

        for i, x in enumerate(nums):
            if i < (n + 1) // 2:
                ans += x * x
            else:
                ans -= x * x

        return ans