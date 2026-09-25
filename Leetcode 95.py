class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:
        memo = {}

        def build_trees(start: int, end: int) -> list[TreeNode | None]:
            if start > end:
                return [None]
            if (start, end) in memo:
                return memo[(start, end)]

            all_trees = []
            # Iterate through each number to act as the root
            for root_val in range(start, end + 1):
                # Generate all possible left and right subtrees
                left_trees = build_trees(start, root_val - 1)
                right_trees = build_trees(root_val + 1, end)

                # Combine every left subtree with every right subtree under root_val
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(root_val, left, right)
                        all_trees.append(root)

            memo[(start, end)] = all_trees
            return all_trees

        return build_trees(1, n)
