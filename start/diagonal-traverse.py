class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        r = 0
        c = 0
        ans = []
        
        dr = "up"
        row = len(mat)
        col = len(mat[0])
        while len(ans) < row*col:
            ans.append(mat[r][c])
            
            if dr =="up":
                if c +1 == col:
                    r+=1
                    dr = "down"
                elif r -1 <0:
                   
                    c+=1
                    dr = "down"
                else:
                    r-=1
                    c +=1
            else:
                if r + 1 == row:
                    c+=1
                    dr = "up"
                elif c -1 <0:
                    
                    r+=1
                    dr = "up"
                
                else:
                    r+=1
                    c-=1
                    
        return ans
                    
                    