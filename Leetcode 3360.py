class Solution:
    def canAliceWin(self, n: int) -> bool:
        remove = 10
        turns = 0
        while n >= remove and remove > 0:
            n -= remove
            remove -= 1
            turns += 1
        return turns % 2 == 1
