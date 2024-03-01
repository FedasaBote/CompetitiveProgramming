class Solution:
    def totalNQueens(self, n: int) -> int:
        matrix = [["." for i in range(n)] for i_ in range(n)]
        ans = []
        def backtrack(row):
            if row == n:
                j = ["".join(a) for a in matrix]
                if j not in ans:
                    ans.append(j)
                return

            for c in range(n):
                if not self.isValid(matrix,row,c):
                    continue
                matrix[row][c] = "Q"
                backtrack(row+1)
                matrix[row][c] = "."

        backtrack(0)

        return len(ans)


    def isValid(self,board,row,col):
        n = len(board)
        if any(board[row][c] != "." for c in range(n)):
            return False
        if any(board[r][col] != "." for r in range(n)):
            return False

        r = row
        c = col
    
        while r < n and c < n:
            if board[r][c] != ".":
                return False
            r += 1
            c += 1

        r = row
        c = col
    
        while r >= 0 and c >= 0:
            if board[r][c] != ".":
                return False
            r -= 1
            c -= 1

        r = row
        c = col
    
        while r >= 0 and c < n:
            if board[r][c] != ".":
                return False
            r -= 1
            c += 1
       
        r = row
        c = col
    
        while r < n and c >= 0:
            if board[r][c] != ".":
                return False
            r += 1
            c -= 1
        
        return True

        