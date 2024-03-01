class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        def backtrack(row,col):
            if row == n:
                return True
            if col ==n:
                return backtrack(row +1,0)
            if board[row][col] != ".":
                return backtrack(row,col + 1)
                
            for i in range(1,10):
                if self.isValid(board,row,col,str(i)):
                    board[row][col] = str(i)
                    if backtrack(row,col +1):
                        return True
                    board[row][col] = "."

            return False
        backtrack(0,0)

    def isValid(self,board,row,col,val):
        n = len(board)
        if any(board[r][col] == val for r in range(n)):
            return False
        if any(board[row][c] == val for c in range(n)):
            return False

        qr = row //3 *3
        qc = col //3 *3

        for i in range(qr,qr +3):
            for j in range(qc,qc +3):
                if board[i][j] == val:
                    return False

        return True

                    