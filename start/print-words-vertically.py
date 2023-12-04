class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        ans =[]
        n = max(map(lambda x:len(x),s.split()))
   
        
        for i in range(n):
            an=""
            for word in s.split():
                if i<len(word):
                    an +=word[i]
                else:
                    an+=" "
            
         
            ans.append(an.rstrip())
            
        return ans
                