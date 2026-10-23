class Solution:
    def isValid(self, s: str) -> bool:
        # Quick check: odd length strings can never be valid
        if len(s) % 2 != 0:
            return False
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping:
                # If stack is empty or the top element doesn't match the required opening bracket
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                stack.append(char)
        return not stack
