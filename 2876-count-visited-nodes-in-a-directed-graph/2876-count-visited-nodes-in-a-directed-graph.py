class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        path={}
        n=len(edges)
        answers=[1 for i in range(n)]
        for i in range(n):
            
            #traverse
            curr=i
            cnt=0
            ok=True
            while curr not in path:
                
                if answers[curr]!=1:
                    ok=False
                    break
                
                path[curr]=cnt
                cnt+=1
                curr=edges[curr]
            
            #print(i,path)
            
            if ok:
                cyclelen = cnt-path[curr]
                cyc_start=path[curr]
                curr=i
                for j in range(cyc_start):
                    answers[curr] = cnt-path[curr]
                    curr=edges[curr]
                for j in range(cyclelen):
                    answers[curr]=cyclelen
                    curr=edges[curr]
            else:
                seen=answers[curr]
                curr=i
                for j in range(cnt):
                    answers[curr] = cnt-path[curr]+seen
                    curr=edges[curr]
            path={}
        return answers
            
                