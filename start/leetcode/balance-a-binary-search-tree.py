# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node:
                inorder(node.left)
                nodes.append(node)
                inorder(node.right)

        def build(s,e):
            if s > e:
                return
            mid = (s + e)//2
            node = nodes[mid]
            node.left=build(s,mid-1)
            node.right= build(mid+1,e)

            return node
        nodes = []
        inorder(root)
        return build(0,len(nodes)-1)
