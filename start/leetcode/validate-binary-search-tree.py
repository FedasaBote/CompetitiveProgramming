# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def helper(root,min_,max_):
            if not root:
                return True
            print(min_,root.val)
            if min_!= None and root.val <= min_:
                return False
            if max_!= None and root.val >= max_:
                return False

            return helper(root.left,min_,root.val) and helper(root.right,root.val,max_)

        return helper(root,None,None)


        