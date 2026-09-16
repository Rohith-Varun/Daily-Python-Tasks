class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        res = []
        
        def dfs(node):
            if not node:
                return
            res.append(node.val)      # Visit root
            dfs(node.left)            # Traverse left
            dfs(node.right)           # Traverse right
            
        dfs(root)
        return res
