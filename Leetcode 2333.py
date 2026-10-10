from typing import List

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        diff.sort(reverse=True)
        n = len(diff)
        diff.append(0)

        for i in range(n):
            cost = (diff[i] - diff[i + 1]) * (i + 1)

            if k >= cost:
                k -= cost
            else:
                level_drop, remainder = divmod(k, i + 1)
                level = diff[i] - level_drop

                for j in range(i + 1):
                    diff[j] = level
                    if j < remainder:
                        diff[j] -= 1

                k = 0
                break

        return sum(x * x for x in diff[:n])