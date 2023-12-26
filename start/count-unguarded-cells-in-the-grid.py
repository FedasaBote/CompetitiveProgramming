class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        matrix = [[""]*n for i in range(m)]
        directions = [(0,1),(-1,0),(0,-1),(1,0)]
        for c in walls:
            x ,y = c
            matrix[x][y] ="W"
            
            
        def mark(cell):
            x, y = cell
            for dr in directions:
                h = "h" if dr[1]==0 else "v"
                while x>=0 and x<m and y>=0 and y<n and matrix[x][y] !="W":
                    if matrix[x][y] ==h:
                        break
                    matrix[x][y] = h
                    x = x+ dr[0]
                    y = y + dr[1]
                x , y = cell
        for cell in guards:
            mark(cell)
        
                
        count = 0
        for r in range(m):
            for c in range(n):
                if matrix[r][c] =="":
                    count+=1
                    
        return count
            
        
        
        