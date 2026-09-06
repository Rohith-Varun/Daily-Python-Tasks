from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        # Dictionary to keep track of counts of all characters in t
        dict_t = Counter(t)
        required = len(dict_t)
        
        # Counter to keep track of how many unique characters are currently matched
        formed = 0
        window_counts = {}
        
        # Tuple format: (window_length, left, right)
        ans = float("inf"), None, None
        l, r = 0, 0
        
        while r < len(s):
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1
                
            while l <= r and formed == required:
                char = s[l]
                
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                    
                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1
                    
                l += 1
                
            r += 1
            
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
