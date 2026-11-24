import math
class Solution:
    def maxLength(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        max_lcm = 2520
        for i in range(n):
            cur_prod = 1
            cur_gcd = 0
            cur_lcm = 1

            for j in range(i, n):
                x = nums[j]
                cur_prod *= x
                cur_gcd = x if cur_gcd == 0 else math.gcd(cur_gcd, x)
                cur_lcm = math.lcm(cur_lcm, x)

                if cur_prod > max_lcm * cur_gcd * cur_lcm:
                    break

                if cur_prod == cur_lcm * cur_gcd:
                    ans = max(ans, j - i + 1)

        return ans
