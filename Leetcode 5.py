class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start = 0
        max_len = 0
        
        def expand(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Length of the palindrome found
            return right - left - 1

        for i in range(len(s)):
            # Check odd-length palindromes centered at s[i]
            len1 = expand(i, i)
            # Check even-length palindromes centered between s[i] and s[i+1]
            len2 = expand(i, i + 1)
            
            length = max(len1, len2)
            
            if length > max_len:
                max_len = length
                # Find starting index of the longest palindrome
                start = i - (length - 1) // 2
                
        return s[start : start + max_len]
