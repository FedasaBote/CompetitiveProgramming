class Solution:
    def isHappy(self, n: int) -> bool:
        
        m ={}
        m[n]=1
        while n!=1:
            n = self.square(n)
            if n in m:
                return False
            m[n]=1
            
        return True
            
            
            
    def square(self,n):
        ans =0
        
        while n>0:
            rem = n%10
            ans+=rem**2
            n//=10
            
        return ans