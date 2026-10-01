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
                # It's an opening bracket
                stack.append(char)

        # Valid only if all opened brackets have been matched and popped
        return not stack
