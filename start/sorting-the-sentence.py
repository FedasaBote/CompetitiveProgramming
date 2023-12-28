class Solution:
    def sortSentence(self, s: str) -> str:
        
        words = s.split()
        m ={}
        for word in words:
            num = int(word[-1])
            word = word[:-1]
            m[num] = word
        
        ans = ""   
        for i in range(1,10):
            if i in m:
                ans += m[i] + " "
                
        return ans.rstrip()
            
            