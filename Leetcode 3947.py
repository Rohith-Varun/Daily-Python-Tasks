from collections import defaultdict
class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        max_f = max(f for f, _ in items)
        freq = [0] * (max_f + 1)
        min_price = float("inf")
        for f, price in items:
            freq[f] += 1
            if price < min_price:
                min_price = price
        multiples = [0] * (max_f + 1)
        for d in range(1, max_f + 1):
            if freq[d]:
                for m in range(d, max_f + 1, d):
                    multiples[d] += freq[m]
        boosted_by_price = defaultdict(int)
        threshold = 2 * min_price
        for f, price in items:
            if price < threshold:
                gain = multiples[f] - 1
                if gain > 0:
                    boosted_by_price[price] += gain
        total_items = 0
        for price in sorted(boosted_by_price):
            if budget < price:
                break
            take = min(boosted_by_price[price], budget // price)
            total_items += 2 * take
            budget -= take * price
        total_items += budget // min_price
        return total_items
