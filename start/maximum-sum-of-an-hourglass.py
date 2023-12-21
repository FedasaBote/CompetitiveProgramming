class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        
        row = 0
        col = 0
        m= len(grid)
        n = len(grid[0])
        total = (m-2)*(n-2)
        res = []
        for r in range(m-2):
            for c in range(n-2):
                tot =0
                for i in range(3):
                    for j in range(3):
                        if (i!=1 or j!=0) and (i!=1 or j!=2):
                            tot+=grid[i+r][j+c]
                        
                res.append(tot)
                
        return max(res)

            
        