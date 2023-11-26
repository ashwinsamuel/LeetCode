class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def dfs(nd,path):
            
            nonlocal result,vis
            
            for ne in graph[nd]:
                if ne not in vis:
                    path.append(ne)
                    vis.add(ne)
                    if ne==n-1: 
                        result.append(path.copy())
                    else:
                        dfs(ne,path)
                    path.pop()
                    vis.remove(ne)
        
        path = [0]
        vis = set([0])
        result = []
        n=len(graph)
        
        dfs(0, path)
        return result
                    
            