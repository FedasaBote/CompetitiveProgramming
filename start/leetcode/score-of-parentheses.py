class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        stack = []

        for i in s:
            if i == "(":
                stack.append(score)
                score = 0
            else:
                if score == 0:
                    score = stack.pop() + 1
                else:
                    score = stack.pop() + score*2


        return score

      
        