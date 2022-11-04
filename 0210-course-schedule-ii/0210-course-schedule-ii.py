class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        result = []
        def dfs(v,visited,path,adj_list):
            visited.add(v)
            for neigh in adj_list[v]:
                if neigh not in visited:
                    path.add(neigh)
                    if not dfs(neigh,visited,path,adj_list):
                        return False
                    path.remove(neigh)
                elif neigh in path:
                    return False
            result.append(v)
            return True
        
        #make graph
        adj_list = []
        for i in range(numCourses):
            adj_list.append([])
        
        for i in range(len(prerequisites)):
            adj_list[prerequisites[i][1]].append(prerequisites[i][0])
            
        visited = set()
        path = set()
        for i in range(numCourses):
            if i not in visited:
                path.add(i)
                if not dfs(i,visited,path,adj_list):
                    return []
                path.remove(i)
        
        return result[::-1]