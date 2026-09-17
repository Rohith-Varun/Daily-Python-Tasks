class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        
        stack = [root]
        result = []
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            # Push left first so right is processed first
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                
        return result[::-1]
