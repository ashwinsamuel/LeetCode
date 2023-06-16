from sortedcontainers import SortedList

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        
        s=0
        presum=[]
        for num in nums:
            s+=num
            presum.append(s)
        
        n=len(nums)
        partition = SortedList([-1,n])
        segs = SortedList([presum[n-1]])
        
        result=[]
        for k in removeQueries:
            
            #remove old
            idx = partition.bisect_right(k)
            r = partition[idx]-1
            l = partition[idx-1]
            tseg = presum[r]-presum[l] if l>=0 else presum[r]
            segs.remove(tseg)
            
            #add 2 new segs
            segs.add(presum[r]-presum[k])
            if k>0:
                segs.add(presum[k-1]-presum[l]) if l>=0 else segs.add(presum[k-1])
            partition.add(k)
            
            
            result.append(segs[-1])
        return result