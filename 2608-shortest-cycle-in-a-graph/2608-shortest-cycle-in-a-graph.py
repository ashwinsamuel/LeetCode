class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        
        adj={i:[] for i in range(n)}
        for e1,e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        
        ans=float('inf')
        
        for i in range(n):
            qu=deque()
            dist={}
            parent={}
            
            qu.append(i)
            dist[i]=0
            parent[i]=-1
            
            while qu:
                nd = qu.popleft()
                for ne in adj[nd]:
                    if ne not in dist:
                        dist[ne]=dist[nd]+1
                        parent[ne]=nd
                        qu.append(ne)
                    elif parent[nd]!=ne:
                        ans=min(ans, dist[nd]+dist[ne]+1 )
        
        return ans if ans!=float('inf') else -1