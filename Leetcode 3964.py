class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        max_factor = max(f for f, _ in items)
        freq = [0] * (max_factor + 1)
        for f, _ in items:
            freq[f] += 1
        dp = [0] * (budget + 1)
        min_price = float("inf")
        for f, price in items:
            if price < min_price:
                min_price = price
            bonus = 0
            for mult in range(f * 2, max_factor + 1, f):
                bonus += freq[mult]
            if freq[f] > 1:
                bonus += freq[f] - 1
            gain = 1 + bonus
            if price <= budget:
                for b in range(budget, price - 1, -1):
                    cand = dp[b - price] + gain
                    if cand > dp[b]:
                        dp[b] = cand
        ans = 0
        for b in range(budget + 1):
            total = dp[b] + (budget - b) // min_price
            if total > ans:
                ans = total

        return ans
