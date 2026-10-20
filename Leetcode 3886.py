
from typing import List

class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True
            prev_max = -1

            for start in range(0, n, k):
                end = start + k
                block_min = nums[start]
                block_max = nums[start]
                drops = 0

                for i in range(start, end):
                    x = nums[i]
                    block_min = min(block_min, x)
                    block_max = max(block_max, x)

                    if i > start and nums[i - 1] > x:
                        drops += 1

                if nums[end - 1] > nums[start]:
                    drops += 1

                if drops > 1 or prev_max > block_min:
                    valid = False
                    break

                prev_max = block_max

            if valid:
                ans += k

        return ans