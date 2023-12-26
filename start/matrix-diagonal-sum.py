class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        total = 0
        
        for i in range(len(mat)):
            total += mat[i][i]
            
        c= len(mat)-1
        r =0
        for i in range(len(mat)):
            total += mat[r][c]
            c-=1
            r+=1
            
        if len(mat)%2!=0:
            n = len(mat)//2
            total -= mat[n][n]
            
        return total
        