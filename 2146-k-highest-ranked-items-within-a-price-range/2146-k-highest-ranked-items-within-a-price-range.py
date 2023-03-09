import heapq
from collections import deque

class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        #K Highest Ranked Items Within a Price Range
        
        def item_add(r,c,grid,items,d,up,lo):
            if lo<= grid[r][c] <=up:
                h = (d,grid[r][c],r,c)
                heapq.heappush(items,h)
            return
        
        #init
        i,j = start
        lo,up=pricing
        items=[]
        vis=set()
        dist={}
        #start should not be 0
        
        #bfs
        qu=deque()
        qu.append((i,j))  #(i,j,vis,items,grid,dist,0)
        
        vis.add((i,j))
        dist[(i,j)] = 0
        item_add(i,j,grid,items,0,up,lo)
        n=len(grid)
        m=len(grid[0])
        while qu:
            r,c = qu.popleft()
            for nei,nej in [(-1,0),(0,-1),(0,1),(1,0)]:
                if 0<=r+nei<n and 0<=c+nej<m and (r+nei,c+nej) not in vis and grid[r+nei][c+nej]>0:

                    ri,cj = r+nei,c+nej
                    vis.add((ri,cj))
                    dist[(ri,cj)] = dist[(r,c)]+1
                    item_add(ri,cj,grid,items, dist[(ri,cj)] ,up,lo)
                    qu.append((r+nei,c+nej))
        
        ans=[]
        while k>0 and items:
            a,b,c,d = heapq.heappop(items)
            ans.append([c,d])
            k-=1
        return ans
        