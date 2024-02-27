# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def helper(root,prev):
            if not root.left and not root.right:
                prev = prev*10 + root.val
                return prev 
            
            prev = prev*10 + root.val
            resl = 0
            resr =0
            if root.left:
                resl = helper(root.left,prev)

            if root.right:
                resr = helper(root.right,prev)
            

            return resl + resr

        return helper(root,0)
            

        