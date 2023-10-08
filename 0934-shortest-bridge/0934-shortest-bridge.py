class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        island_one = set()

        rows, cols = len(grid), len(grid[0])

        def is_valid_child(child_row, child_col):
            return (0 <= child_row < rows) and (0 <= child_col < cols) and \
            (child_row, child_col) not in island_one
        
        def dfs(curr_row, curr_col):
            stack = [(curr_row, curr_col)]
            island_one.add((curr_row, curr_col))

            while stack:
                curr_row, curr_col =  stack.pop()

                #island_one.add((curr_row, curr_col))
                possible_dir = [(curr_row+1, curr_col), (curr_row, curr_col+1), (curr_row-1, curr_col), (curr_row, curr_col-1)]

                for child_row, child_col in possible_dir:
                    if is_valid_child(child_row, child_col) and grid[child_row][child_col] == 1:
                        stack.append((child_row, child_col))
                        island_one.add((child_row, child_col))
            
            return


        dfs_done = False
        for row in range(rows):
            
            for col in range(cols):
                if grid[row][col] == 1:
                    dfs(row, col)
                    dfs_done = True
                    break
            
            if dfs_done:
                break
        
        # Doing BFS
        queue = deque([val for val in island_one])
        flip = 0

        #print(queue)
        while queue:
            for val in range(len(queue)):
                curr_row, curr_col = queue.popleft()
                

                # if grid[curr_row][curr_col] == 1 and (curr_row, curr_col) not in island_one:
                #     return flip
                
                #island_one.add((curr_row, curr_col)) # works as a visit set
                
                possible_dir = [(curr_row+1, curr_col), (curr_row, curr_col+1), (curr_row-1, curr_col), (curr_row, curr_col-1)]

                for child_row, child_col in possible_dir:
                    if is_valid_child(child_row, child_col):
                        if grid[child_row][child_col] == 1:
                            return flip
                        queue.append((child_row, child_col))
                        island_one.add((child_row, child_col))
            
            flip += 1
        

        return -1