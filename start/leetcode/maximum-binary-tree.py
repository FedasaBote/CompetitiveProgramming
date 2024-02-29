# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def maxIndex(arr):
            max_ = 0
            for i in range(len(arr)):
                if arr[i] > arr[max_]:
                    max_ = i

            return max_

        def helper(arr,root,dr):
            # if len(arr) == 1:
            #     if dr == 1:
            #         root.right = TreeNode(arr[0])
            #     else: root.left = TreeNode(arr[0]) 
            #     return
            if len(arr) == 0:
                return
            max_ = maxIndex(arr)
            if dr == 0:
                root.left = TreeNode(arr[max_])
                helper(arr[:max_],root.left,0)
                helper(arr[max_+1:],root.left,1)
            elif dr == 1:
                root.right = TreeNode(arr[max_])
                helper(arr[:max_],root.right,0)
                helper(arr[max_+1:],root.right,1)
            else:
                root = TreeNode(arr[max_])
                helper(arr[:max_],root,0)
                helper(arr[max_+1:],root,1)
           
            return root

        return helper(nums,None,-1)
    
            

        