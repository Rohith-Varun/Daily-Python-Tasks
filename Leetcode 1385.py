from bisect import bisect_left

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        m = len(arr2)
        count = 0
        for x in arr1:
            i = bisect_left(arr2, x - d)  # first element >= x - d
            # If it exists and is <= x + d, then |x - arr2[i]| <= d → x is invalid
            if i == m or arr2[i] > x + d:
                count += 1
        return count