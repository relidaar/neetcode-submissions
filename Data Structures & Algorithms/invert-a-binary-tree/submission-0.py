# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def getVal(node):
    return node.val if node else None

def invert(root):
    if not root:
        return
    invert(root.left)
    invert(root.right)
    root.left, root.right = root.right, root.left

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        invert(root)
        return root