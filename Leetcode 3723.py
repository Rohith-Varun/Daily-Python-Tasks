class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""

        if sum == 0:
            return "0" if num == 1 else ""

        digits = []
        remaining = sum

        for _ in range(num):
            digit = min(9, remaining)
            digits.append(str(digit))
            remaining -= digit

        if remaining > 0:
            return ""

        return "".join(digits)