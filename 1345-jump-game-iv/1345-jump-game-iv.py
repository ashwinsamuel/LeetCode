class Solution:
    def minJumps(self, arr: List[int]) -> int:
        que = deque([])
        que.append((0,0))
        n=len(arr)
        visi = set()
        
        #build map
        mp={}
        for i in range(n):
            if arr[i] not in mp:
                mp[arr[i]] = [-i]
            else:
                heapq.heappush(mp[arr[i]],-i)
        
        while que:
            idx,steps=que.popleft()
            
            if idx==n-1:
                return steps
            
            while mp[arr[idx]]:
                neigh = -heapq.heappop(mp[arr[idx]])
                if neigh not in visi:
                    que.append((neigh,steps+1))
                    visi.add(neigh)
            
            if idx+1<n and idx+1 not in visi:
                que.append((idx+1,steps+1))
                visi.add(idx+1)
            
            if idx-1>=0 and idx-1 not in visi:
                que.append((idx-1,steps+1))
                visi.add(idx-1)
        
        return -1
            
            