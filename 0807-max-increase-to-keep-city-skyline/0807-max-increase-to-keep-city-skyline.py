class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        n=len(grid)
        maxRow=[]
        maxCol = [0 for i in range(n)]
        for i in range(n):
            maxRow.append(max(grid[i][:]))
            for j in range(n):
                maxCol[i]=max(maxCol[i] , grid[j][i])

        ans=0
        for i in range(n):
            for j in range(n):
                tmin=min(maxRow[i],maxCol[j])
                ans+=tmin-grid[i][j]
        return ans