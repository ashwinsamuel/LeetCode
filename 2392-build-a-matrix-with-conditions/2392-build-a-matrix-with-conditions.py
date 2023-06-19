class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        #2*top sort -> O(2*k+n+m)
        #k^2
        #print(k)
        #1:k for adj list
        rr,cc = {},{}
        for x,y in rowConditions:
            rr[x] = rr.get(x,[]) + [y]
        for x,y in colConditions:
            cc[x] = cc.get(x,[]) + [y]
            
            
        #print(k)
        
        #0:k-1 for in_degree
        inr,inc=[0 for i in range(k)],[0 for i in range(k)]
        for ke,ll in rr.items():
            for ne in ll:
                inr[ne-1] +=1
        rq=deque()
        #print(k)
        for i in range(k):
            #print(i,inr[i])
            if inr[i]==0:
                rq.append(i+1)
                #print(i+1)
        
        #print(rq)
        
        for ke,ll in cc.items():
            for ne in ll:
                inc[ne-1] +=1
        cq=deque()
        for i in range(k):
            if inc[i]==0:
                cq.append(i+1)

        #CHECK IF COULDVE USED 1-K
        #print(rq,inr)
        rrr=[]
        while rq:
            idx = rq.popleft()
            rrr.append(idx)
            for ne in rr.get(idx,[]):
                inr[ne-1]-=1
                if inr[ne-1]==0:
                    rq.append(ne)
        #print(rrr)
        if len(rrr)!=k:
            return []
        
        ccc=[]
        while cq:
            idx = cq.popleft()
            ccc.append(idx)
            for ne in cc.get(idx,[]):
                inc[ne-1]-=1
                if inc[ne-1]==0:
                    cq.append(ne)
    
        #print(ccc)
    
        if len(ccc)!=k:
            return []
        
        
    
        
        
        result = [[0 for i in range(k)] for i in range(k)]
        order1={}
        order2={}
        for i in range(k):
            order1[ rrr[i] ] = i
            order2[ ccc[i] ] = i
        
        for i in range(k):
            result[order1[i+1]][order2[i+1]] = i+1
        
        return result
        
        
        
        
        
        
        
        
        
        