class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:

        prev = 0
        for row in grid:
            prev += sum(row)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = min(self.givemax(grid,j),max(grid[i]))

        print(grid)

        score =0
        for row in grid:
            score += sum(row)
        
        return score - prev

    def givemax(self,grid,col):
        max_ = float("-inf")
        for i in range(len(grid)):
            max_ = max(grid[i][col],max_)

        return max_
