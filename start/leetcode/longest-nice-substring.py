class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def is_nice(sub):
            return all(c.swapcase() in sub for c in sub)


        max_len = 0
        result = ""
        n = len(s)
        
        for i in range(n):
            for j in range(i + 1, n + 1):
                sub = s[i:j]
                if is_nice(sub) and len(sub) > max_len:
                    max_len = len(sub)
                    result = sub
        
        return result