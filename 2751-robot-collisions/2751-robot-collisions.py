class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        
        n=len(positions)
        sposition = sorted([(positions[i],i) for i in range(n)])
        #case when same pos
        
        stack=[]
        rmvd=set()
        for pos,i in sposition:
            if directions[i] == 'R':
                stack.append(i)
            else:
                while len(stack)>0 and healths[i] > healths[stack[-1]]:
                    rmvd.add(stack.pop())
                    healths[i]-=1
                
                if len(stack)>0:
                    rmvd.add(i)
                    if healths[i]==healths[stack[-1]]:
                        rmvd.add(stack.pop())
                    else:
                        healths[stack[-1]]-=1

        result=[]
        for i in range(n):
            if i not in rmvd:
                result.append(healths[i])
        
        return result