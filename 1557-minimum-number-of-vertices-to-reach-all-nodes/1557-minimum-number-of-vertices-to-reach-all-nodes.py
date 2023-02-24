class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        not_src = set()
        
        for s,t in edges:
            not_src.add(t)
        result=[]
        for v in range(n):
            if v not in not_src:
                result.append(v)
        return result