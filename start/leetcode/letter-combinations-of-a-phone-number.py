class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        map_ = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        ans = []
        stack = []
        
        def backtrack(idx, lidx):
            if idx == len(digits):
                ans.append("".join(stack))
                return
            for j in range(lidx, len(map_[int(digits[idx])])):
                stack.append(map_[int(digits[idx])][j])
                backtrack(idx + 1, 0)
                stack.pop()

        backtrack(0, 0)

        return ans
                
        