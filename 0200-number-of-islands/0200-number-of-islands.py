class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(cell):
            stack = [cell]

            while stack:
                ele = stack.pop()
                grid[ele[0]][ele[1]] = "0"

                #neighbours
                n = []
                if ele[0] > 0 and grid[ele[0] - 1][ele[1]] == "1":
                    n.append((ele[0] - 1, ele[1]))
                if ele[1] > 0 and grid[ele[0]][ele[1]-1] == "1":
                    n.append((ele[0], ele[1]-1))
                if ele[0] < rows-1 and grid[ele[0] + 1][ele[1]] == "1":
                    n.append((ele[0]+1, ele[1]))
                if ele[1] < cols-1 and grid[ele[0]][ele[1]+1] == "1":
                    n.append((ele[0], ele[1]+1))

                for neighbour in n:
                    stack.append(neighbour)
        
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs((i,j))
                    count += 1
        return count
                
                
                
                
        