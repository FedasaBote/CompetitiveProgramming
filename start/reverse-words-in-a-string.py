class Solution:
    def reverseWords(self, s: str) -> str:
        strings = s.strip().split()
        
        ans =[]
        
        for i in strings:
            ans.append(i.strip())
            
        return " ".join(ans[::-1])
        