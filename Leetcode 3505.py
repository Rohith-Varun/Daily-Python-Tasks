from typing import List
class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        vals = sorted(set(nums))
        idx = {v: i + 1 for i, v in enumerate(vals)}
        m = len(vals)
        cnt = [0] * (m + 1)
        sm = [0] * (m + 1)
        LOG = m.bit_length()
        def upd(i, c, s):
            while i <= m:
                cnt[i] += c
                sm[i] += s
                i += i & -i
        kk = (x + 1) // 2  
        def window_cost(total):
            pos = c = s = 0
            for p in range(LOG, -1, -1):
                np_ = pos + (1 << p)
                if np_ <= m and c + cnt[np_] < kk:
                    pos = np_
                    c += cnt[np_]
                    s += sm[np_]
            v = vals[pos]
            left = s + (kk - c) * v
            right = total - left
            return v * kk - left + right - v * (x - kk)
        cost = []
        total = 0
        for i in range(n):
            upd(idx[nums[i]], 1, nums[i])
            total += nums[i]
            if i >= x:
                upd(idx[nums[i - x]], -1, -nums[i - x])
                total -= nums[i - x]
            if i >= x - 1:
                cost.append(window_cost(total))
        INF = float('inf')
        prev = [0] * (n + 1)
        for _ in range(k):
            cur = [INF] * (n + 1)
            for i in range(x, n + 1):
                cur[i] = min(cur[i - 1], prev[i - x] + cost[i - x])
            prev = cur
        return prev[n]
