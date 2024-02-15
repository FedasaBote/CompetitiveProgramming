class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c5 = 0
        c10 = 0

        for i in bills:
            if i==5:
                c5 +=1
            elif i == 10:
                if c5 == 0:
                    return False
                c5 -= 1
                c10 +=1
            else:
                if c10 >0 and c5 >0:
                    c5 -=1
                    c10 -=1
                elif c5 >2:
                    c5 -=3
                else:
                    return False
            
        return True