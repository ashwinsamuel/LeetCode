from sortedcontainers import SortedList

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        
        squeries = sorted(queries)
        slogs = sorted(logs,key = lambda x:x[1])
        
        
        l,r=0,0
        cnt = {}
        vis=set()
        ans={}
        for q in squeries:
        
            #add r
            while r<len(slogs) and slogs[r][1]<=q:
                idx = slogs[r][0]
                r+=1
                cnt[idx] = cnt.get(idx,0)+1
                vis.add(idx)
            
            #remove l
            while l< len(slogs) and slogs[l][1]<q-x:
                idx = slogs[l][0]
                l+=1
                cnt[idx]-=1
                if cnt[idx]==0:
                    vis.remove(idx)
            
            ans[q] = n-len(vis)
            #print(q,cnt)
        
        result=[]
        for q in queries:
            result.append(ans[q])
            
        return result