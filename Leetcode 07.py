class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        while x != 0:
            pop = x % 10
            x //= 10
            
            # Check 32-bit signed integer overflow prior to calculation
            if res > (INT_MAX - pop) // 10:
                return 0
            
            res = res * 10 + pop
            
        return res * sign
      
