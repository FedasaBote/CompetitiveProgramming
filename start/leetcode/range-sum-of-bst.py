# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        arr= [0]
        def helper(root):
            if root:
                if root.val >= low and root.val <= high:
                    arr[0] += root.val
                helper(root.left)
                helper(root.right)


        helper(root)
        return arr[0]                

    
                
        