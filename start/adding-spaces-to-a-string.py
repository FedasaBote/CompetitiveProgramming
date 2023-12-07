class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans=""
        prev=0
        for i in spaces:
            ans+=s[prev:i]
            ans+=" "
            prev=i
        ans+=s[prev:]
            
        return ans
        