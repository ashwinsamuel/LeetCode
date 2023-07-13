class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        
        n=len(nums)
        chg = [0]*(n+1)
        tsum = 0
        for i in range(n):
            
            tsum = chg[i]+tsum
            nums[i]+=tsum
            if nums[i]<0:
                return False
            
            if i+k<=n:
                tsum-=nums[i]
                chg[i+k]=nums[i]
                nums[i]=0
            else:
                if nums[i]!=0:
                    print(i,nums)
                    return False
        print(nums)
        
        return True
            