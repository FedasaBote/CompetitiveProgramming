# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(root):
            if root:
                traverse(root.left)
                frequencies[root.val] += 1
                traverse(root.right)


        frequencies = defaultdict(int)
        traverse(root)
        max_ = max(frequencies.values()) if frequencies else 0
        mode = [key for key,val in frequencies.items() if val == max_]

        return mode

        


        