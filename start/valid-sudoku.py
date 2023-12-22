class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        for r in range(len(board)):
            row = {}
            for el in board[r]:
                if el in row and el !=".":
                    return False
                row[el] =1
                
            col = {}
            
            for i in range(9):
                if board[i][r] in col and board[i][r] !=".":
                    return False
                col[board[i][r]] = 1
                
                
        for i in range(3):
            for j in range(3):
                sub = {}
                for k in range(3):
                    for l in range(3):
                        if board[i*3+l][j*3+k] in sub and board[i*3+l][j*3+k] !=".":
                            return False
                        sub[board[i*3+l][j*3+k]] =1
                        
                        
        return True
                        
        
        
                    
        