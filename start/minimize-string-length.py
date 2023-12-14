class Solution:
    def minimizedStringLength(self, s: str) -> int:
        
        mp ={}
        
        for i in s:
            mp[i]=1
            
        return len(mp)
        