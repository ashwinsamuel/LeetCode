class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        n=len(basket1)
        
        total = basket1+basket2
        MIN = min(total)
        total = Counter(total)
        cnt1,cnt2 = Counter(basket1),Counter(basket2)
        
        basket1.sort()
        basket2.sort(reverse=True)
        from2,from1=[],[]
        
        done=set()
        for val in basket1:
            if total[val]%2==1: return -1
            if val not in done and cnt1[val]>total[val]//2:
                diff = cnt1[val] - total[val]//2
                #print(val,diff)
                from1.extend([val]*diff)
                done.add(val)
                
        done=set()
        for val in basket2:
            if total[val]%2==1: return -1
            if val not in done and cnt2[val]>total[val]//2:
                diff = cnt2[val] - total[val]//2
                from2.extend([val]*diff)
                done.add(val)
        
        if len(from1)!=len(from2): return -1
        
        '''
        print(from1)
        print(cnt1)
        print(from2)
        print(cnt2)
        print(total)
        '''
        
        
        ans=0
        for i in range(len(from1)):
            if min(from1[i],from2[i])<2*MIN:
                ans+=min(from1[i],from2[i])
            else:
                ans+=2*MIN
        return ans
            
                
            