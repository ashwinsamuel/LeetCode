class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        prefix = [0]
        n=len(nums)
        
        for i in range(n):
            prefix.append(prefix[-1]+nums[i])
            
        k = prefix[-1] #total 1s
        
        #find window of size k with max no of 1s
        tmax=-1
        for i in range(n):
            if i+k<=n:
                temp = prefix[i+k]-prefix[i]
            else:
                temp = (prefix[n]-prefix[i]) + (prefix[i+k-n] -prefix[0])
            if temp>tmax:
                tmax=temp
        return k-tmax
        
        