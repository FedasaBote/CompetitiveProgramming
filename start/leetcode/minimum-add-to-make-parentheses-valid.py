class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for p in s:
            if p == ")":
                if stack and stack[-1] =="(":
                    stack.pop()
                else:
                    stack.append(p)
            else:
                stack.append(p)

        return len(stack)
                
        