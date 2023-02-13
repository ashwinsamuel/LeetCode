from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        que = deque([])
        que.append(start)
        n=len(arr)
        visited = set()
        
        while que:
            idx = que.popleft()
            
            if arr[idx]==0:
                return True
            
            if idx+arr[idx] < n and idx+arr[idx] not in visited:
                que.append(idx+arr[idx])
                visited.add(idx+arr[idx])
                
            if idx-arr[idx] >= 0 and idx-arr[idx] not in visited:
                que.append(idx-arr[idx])
                visited.add(idx-arr[idx])
        
        return False
                
            