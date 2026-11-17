class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        divs = [[] for _ in range(n + 1)]
        for length in range(1, n + 1):
            for d in range(1, length):
                if length % d == 0:
                    divs[length].append(d)
        def palindrome_changes(sub):
            changes = 0
            l, r = 0, len(sub) - 1
            while l < r:
                if sub[l] != sub[r]:
                    changes += 1
                l += 1
                r -= 1
            return changes
        cost = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                min_c = float("inf")
                for d in divs[length]:
                    current_cost = 0
                    for start in range(d):
                        group = []
                        for idx in range(start, length, d):
                            group.append(s[i + idx])
                        current_cost += palindrome_changes(group)
                    min_c = min(min_c, current_cost)
                cost[i][j] = min_c
        # Memoized DP: dp(i, rem) -> min changes for s[i:] into rem parts
        memo = {}

        def dp(i, rem):
            if rem == 1:
                return cost[i][n - 1]
            if (i, rem) in memo:
                return memo[(i, rem)]

            ans = float("inf")
            # Try all possible ending points x for the first of the 'rem' substrings
            # Ensure remaining characters are enough for the remaining (rem - 1) parts
            for x in range(i, n - rem):
                ans = min(ans, cost[i][x] + dp(x + 1, rem - 1))

            memo[(i, rem)] = ans
            return ans

        return dp(0, k)
