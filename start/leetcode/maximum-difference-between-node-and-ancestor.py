# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def helper(min_,max_,root):
            if not root:
                return max_ - min_
            
            return max(
                helper(min(root.val, float('inf') if min_ is None else min_),
                max(root.val,float('-inf') if max_ is None else max_),root.left),
                helper(min(root.val, float('inf') if min_ is None else min_),
                max(root.val,float('-inf') if max_ is None else max_),root.right))

        return helper(None,None,root)

        