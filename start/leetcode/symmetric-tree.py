# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        

        ls = deque()
        ls.append((1,root.left))
        ls.append((1,root.right))

        while ls:

            ans = []
            level,node = ls.popleft()

            if node:
                ls.append((level+1,node.left))
                ls.append((level+1,node.right))

            ans.append(node)

            while ls and ls[0][0] == level:
                l,n= ls.popleft()
                if n:
                    ls.append((l+1,n.left))
                    ls.append((l+1,n.right))

                ans.append(n)

            left = 0
            right = len(ans) -1
            while left < right:
                if ans[left] and ans[right] and ans[left].val != ans[right].val:
                    return False

                if((not ans[left] and ans[right]) or (not ans[right] and ans[left])):
                    return False

                left += 1
                right -= 1

        return True  

        