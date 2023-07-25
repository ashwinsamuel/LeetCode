import heapq

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        
        #exception
        if grid[0][1]>1 and grid[1][0]>1:
            return -1
        
        
        nes = [(+1,0),(-1,0),(0,+1),(0,-1)]
        qu = [(0,0,0)]
        m,n = len(grid),len(grid[0])
        vis = set([(0,0)])

        while qu:
            time, i , j = heapq.heappop(qu)
            
            if i==m-1 and j==n-1:
                return time
            
            for dx,dy in nes:
                nei,nej = i+dx,j+dy
                if 0<=nei<m and 0<=nej<n and (nei,nej) not in vis:
                    vis.add((nei,nej))
                    #print(i,j)
                    if time+1>=grid[nei][nej]:
                        heapq.heappush(qu,(time+1,nei,nej))
                    else:
                        mul = (grid[nei][nej] - time)//2
                        heapq.heappush(qu,(time+2*mul + 1,nei,nej))
        
        return -1
            