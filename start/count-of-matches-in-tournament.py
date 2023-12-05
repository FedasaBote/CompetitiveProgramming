class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        plays =0
        while n>0:
            if n==1:
                break
            
            if n%2==0:
                plays+=n//2
                n = n//2
               
            else:
                plays +=(n-1)//2
                n = (n-1)//2 +1
               
            
                
        return plays
            
        