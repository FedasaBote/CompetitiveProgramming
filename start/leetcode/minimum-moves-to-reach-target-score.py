class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:

        c = 0

        while target >1:
            if maxDoubles > 0:

                if target % 2 ==0:
                    target = target //2
                    maxDoubles -=1
                
                else:
                    target -=1
                c += 1
            else:
                c += target -1
                target = 1
        return c
       