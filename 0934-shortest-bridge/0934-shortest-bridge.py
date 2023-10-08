class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n=len(grid[0])
        
        def dfs(vis,i,j):
            
            vis.add((i,j))
            for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                nei = i+dx
                nej = j+dy
                if 0<=nei<n and 0<=nej<n and grid[nei][nej]==1 and (nei,nej) not in vis:
                    dfs(vis,nei,nej)
                    
                    
            
        
        
        island1=set()
        ok=False
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    dfs(island1,i,j)
                    ok=True
                    break
            if ok: break
                    
        
        #bfs
        qu=deque()
        for (i,j) in island1:
            qu.append((i,j,0))
        
        #print(qu)
        
        vis=set()
        while qu:
            x,y,d = qu.popleft()
            
            for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                nex = x+dx
                ney = y+dy
                if 0<=nex<n and 0<=ney<n and (nex,ney) not in island1 and (nex,ney) not in vis:
                    
                    if grid[nex][ney]==1:
                        return d
                    
                    qu.append((nex,ney,d+1))
                    vis.add((nex,ney))
            #print(qu)
        #return -1
                    
        