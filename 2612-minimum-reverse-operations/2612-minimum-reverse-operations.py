from sortedcontainers import SortedList
from collections import deque

class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        banned=set(banned)
        unvisited=[SortedList([]),SortedList([])]
        for i in range(n):
            if i not in banned:
                unvisited[i%2].add(i)
            
        result = [-1]*n
        
        que = deque([(p,0)])
        result[p]=0
        unvisited[p%2].remove(p)
        
        while que:
            nd,d = que.popleft()
            lo = max(nd-k+1,0)
            lo=2*lo-nd+k-1
            hi=min(nd+k-1,n-1)
            hi=2*hi-k-nd+1
            
            for ne in list(unvisited[(nd+k-1)%2].irange( lo , hi ) ): #2
                que.append((ne,d+1))
                result[ne]=d+1
                unvisited[(nd+k-1)%2].remove(ne)
        
        return result