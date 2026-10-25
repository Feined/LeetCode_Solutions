class Solution:
    def dfs(self,grid,r,c,m,n):
        if r>=m or r<0 or c>=n or c<0:
            return False
        if grid[r][c]==1:
            return True
        grid[r][c] = 1
        left_closed = self.dfs(grid,r,c-1,m,n)
        right_closed = self.dfs(grid,r,c+1,m,n)
        up_closed = self.dfs(grid,r-1,c,m,n)
        down_closed = self.dfs(grid,r+1,c,m,n)
        return left_closed and right_closed and up_closed and down_closed
    def closedIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    if self.dfs(grid,i,j,m,n) == True:
                        res+=1
        return res