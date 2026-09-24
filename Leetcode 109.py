class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # 1. Convert linked list to an array
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        
        # 2. Recursively build height-balanced BST from array
        def build_bst(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(vals[mid])
            root.left = build_bst(left, mid - 1)
            root.right = build_bst(mid + 1, right)
            return root
        
        return build_bst(0, len(vals) - 1)
