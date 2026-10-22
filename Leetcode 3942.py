class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
            
        target_inc = list(range(n))
        target_dec = list(range(n - 1, -1, -1))
        
        # Helper to check if arr is a cyclic shift of target and return the shift amount
        def get_shift(arr, target):
            # Find where target[0] appears in arr
            val = target[0]
            try:
                start_idx = arr.index(val)
            except ValueError:
                return -1
                
            # Verify if the rest of the array matches the cyclic shift
            for i in range(n):
                if arr[(start_idx + i) % n] != target[i]:
                    return -1
            return start_idx

        ans = float('inf')
        
        # Case 1: Increasing cyclic shift
        shift_inc = get_shift(nums, target_inc)
        if shift_inc != -1:
            # Option A: Rotate left `shift_inc` times
            ans = min(ans, shift_inc)
            # Option B: Reverse -> Rotate -> Reverse
            ans = min(ans, 2 + (n - shift_inc) % n)

        # Case 2: Decreasing cyclic shift
        shift_dec = get_shift(nums, target_dec)
        if shift_dec != -1:
            # Option A: Reverse first, then rotate
            ans = min(ans, 1 + (n - shift_dec) % n)
            # Option B: Rotate first, then reverse
            ans = min(ans, shift_dec + 1)

        return ans if ans != float('inf') else -1
