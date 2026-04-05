# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None


        def reverse(root: Optional[TreeNode]) -> Optional[TreeNode]:
            if not root:
                return None

            tmp = root.left
            root.left = root.right
            root.right = tmp
            reverse(root.left)
            reverse(root.right)
            return root

        return reverse(root)        