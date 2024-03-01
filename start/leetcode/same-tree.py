# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def helper(p,q):
            if not p and not q:
                return True
            if (not p and q) or (not q and p)  or (p.val != q.val):
                return False

            ans = helper(p.left,q.left)
            ans1 = helper(p.right,q.right)

            return ans1 and ans

        return helper(p,q)
        