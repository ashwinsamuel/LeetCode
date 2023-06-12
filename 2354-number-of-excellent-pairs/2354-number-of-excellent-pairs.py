from sortedcontainers import SortedList

class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        #n(a) + n(b)
        #[2,3,4,1,...]   sum of 2 cnt+prev >=k      if distinct +=2 else +=1
        #cnt-k >= -prev
        
        nbits = []
        vis=set()
        for i,num in enumerate(nums):
            if num not in vis:
                nbits.append( (num.bit_count(),i) )
                vis.add(num)
        
        nbits = SortedList(nbits)
        
        print(nbits)
        
        #distinct
        ans=0
        n=len(nbits)
        for num,i in nbits:
            idx = nbits.bisect_left( (k-num,-1) ) #when neg
            ans += (n-idx)
            print(n-idx)
        
        return ans
        
        
        
        
        
            