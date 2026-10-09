class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        open_count = 0
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == '(':
                open_count += 1
                i += 1
            else:
                # Check if we have two consecutive closing brackets '))'
                if i + 1 < n and s[i + 1] == ')':
                    i += 2
                else:
                    # Missing one ')', so insert one
                    insertions += 1
                    i += 1
                
                # Match with an open bracket '(' if available
                if open_count > 0:
                    open_count -= 1
                else:
                    # Missing an open bracket '(', so insert one
                    insertions += 1
        
        # Any unmatched '(' requires two ')' brackets each
        insertions += open_count * 2
        return insertions
