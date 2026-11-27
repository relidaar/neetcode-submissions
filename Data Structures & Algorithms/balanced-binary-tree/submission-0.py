# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def rec(root) -> tuple[int, bool]:
            if not root:
                return 0, True
            leftHeight, leftIsBalanced = rec(root.left)
            rightHeight, rightIsBalanced = rec(root.right)
            return 1 + max(leftHeight, rightHeight), \
                    leftIsBalanced and rightIsBalanced \
                    and abs(leftHeight - rightHeight) <= 1
        return rec(root)[1]