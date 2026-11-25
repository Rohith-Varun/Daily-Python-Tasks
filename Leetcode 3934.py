from collections import Counter
from typing import List
class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        mod1, mod2 = 1000000007, 1000000009
        base1, base2 = 100003, 100019
        p1 = [1] * (n + 1)
        p2 = [1] * (n + 1)
        h1 = [0] * (n + 1)
        h2 = [0] * (n + 1)
        for i, val in enumerate(nums):
            p1[i + 1] = (p1[i] * base1) % mod1
            p2[i + 1] = (p2[i] * base2) % mod2
            h1[i + 1] = (h1[i] * base1 + val) % mod1
            h2[i + 1] = (h2[i] * base2 + val) % mod2
        def get_hash(l: int, r: int) -> tuple[int, int]:
            x1 = (h1[r] - h1[l] * p1[r - l]) % mod1
            x2 = (h2[r] - h2[l] * p2[r - l]) % mod2
            return (x1, x2)
        def has_unique_of_len(k: int) -> bool:
            freq = Counter(get_hash(i, i + k) for i in range(n - k + 1))
            return any(cnt == 1 for cnt in freq.values())
        lo, hi = 1, n
        ans = n
        while lo <= hi:
            mid = (lo + hi) // 2
            if has_unique_of_len(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return ans
