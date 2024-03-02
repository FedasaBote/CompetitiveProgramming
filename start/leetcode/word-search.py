class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path =set()
        def backtrack(parent,path,next):
            if(next==len(word)): return True
            directions = [[0,-1],[0,1],[1,0],[-1,0]]
          
            for dir in directions:
                row= parent[0]+dir[0]
                col=parent[1]+dir[1]
                if(self.valid(row,col,board)  and board[row][col]==word[next] and not (row,col) in path):
                    path.add((row,col))
                    result = backtrack([row,col],path,next+1)
                    if(result):
                        return True
                    else:
                        path.remove((row,col))
            
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j]==word[0]):
                    path.add((i,j))
                    if(backtrack([i,j],path,1)):
                        return True
                    path.remove((i,j))
        return False
    
    def valid(self,row, col,board):
        return row>=0 and col>=0 and row<len(board) and col<len(board[0]) 
                

