class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0]*cols for _ in range(rows)]

        for i in range(rows):
            dp[i][0] = 1
        
        maxmoves = 0

        for j in range(1,cols):
            for i in range(rows):
                if grid[i][j] > grid[i][j-1] and dp[i][j-1]>0:
                   dp[i][j] = max(dp[i][j], dp[i][j-1]+1)

                if i - 1>=0 and grid[i][j] > grid[i-1][j-1] and dp[i-1][j-1]>0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)

                if i+1<rows and grid[i][j] > grid[i+1][j-1] and dp[i+1][j-1]>0:
                    dp[i][j] = max(dp[i][j], dp[i+1][j-1]+1)

                maxmoves = max(maxmoves, dp[i][j]-1)

        return maxmoves