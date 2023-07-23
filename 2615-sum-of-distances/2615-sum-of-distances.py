class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        
        cnt={}
        n=len(nums)
        for i,num in enumerate(nums):
            if num not in cnt:
                cnt[num]=[]
            cnt[num].append(i)
        
        result=[0]*n
        
        for k,ll in cnt.items():
            n=len(ll)
            tsum,prefix=sum(ll),0
            
            for i in range(n):
                idx = ll[i]
                tsum-=idx
                result[idx] = (tsum - (n-i-1)*idx) + (i*idx - prefix)
                prefix+=idx
                
        
        return result
            
            
            