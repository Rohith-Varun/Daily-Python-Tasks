from string import ascii_lowercase

class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        # Linear sortedness check via counting (26 fast C-level passes)
        if s == "".join(c * s.count(c) for c in ascii_lowercase):
            return 0
        if n == 2:
            return -1

        mn, mx = min(s), max(s)

        if s[0] == mn or s[-1] == mx:
            return 1

        if s[0] == mx and s[-1] == mn and s.count(mn) == 1 and s.count(mx) == 1:
            return 3

        return 2