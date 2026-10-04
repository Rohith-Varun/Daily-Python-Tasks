class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0   # Minimum possible count of open '('
        high = 0  # Maximum possible count of open '('
        
        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                low -= 1
                high -= 1
            else:  # char == '*'
                low -= 1   # Treat '*' as ')'
                high += 1  # Treat '*' as '('
            
            # If high drops below 0, there are unmatched ')'
            if high < 0:
                return False
            
            # Reset low if it goes negative (treating '*' as empty instead of ')')
            low = max(low, 0)
            
        # Return boolean directly without trailing comma
        return low == 0
