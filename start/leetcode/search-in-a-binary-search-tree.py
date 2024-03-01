# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def helper(root):
            if not root:
                return

            if root.val == val:
                return root

            ans = helper(root.left)
            ans2 = helper(root.right)

            return ans or ans2

        return helper(root)



        