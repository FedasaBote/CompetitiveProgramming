class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        
        out =0
        h = 0
        c= 0
        for i in flips:
            out +=1
            h = max(h,i)
            
            if out ==h:
                c+=1
                
        return c
        