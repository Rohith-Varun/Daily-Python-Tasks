from itertools import accumulate
class Solution:
  def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
    pref = list(accumulate(nums, initial=0))
    n = len(nums)
    return min(
        ( diff
            for i in range(n - l + 1)
            for p_j in pref[i + l : i + r + 1]
            if (diff := p_j - pref[i]) > 0
        ),
        default=-1,
    )
