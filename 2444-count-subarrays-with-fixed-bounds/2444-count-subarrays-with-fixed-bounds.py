class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        if minK>maxK: return 0
        
        #break into partitions free of obstructions
        n=len(nums)
        prevl=-1
        obstruct = []
        for i,num in enumerate(nums):
            if num<minK or num>maxK:
                if prevl!=-1:
                    obstruct.append([prevl,i-1])
                    prevl=i+1
            elif prevl==-1:
                prevl=i

        if prevl!=n and prevl!=-1:
            obstruct.append([prevl,n-1])
            
        print(obstruct)
        
        cnt,ans=0,0
        while cnt<len(obstruct):
            #for each partition
            l,r = obstruct[cnt][0] , obstruct[cnt][1]
            ok=False
            validCnt = 0
            r_min , r_max=-1,-1
            
            for i in range(l,r+1):
                if not ok:
                    if nums[i]==minK:
                        r_min=i
                        if maxK==minK: r_max=i
                    elif nums[i]==maxK:
                        r_max=i

                    if min(r_min,r_max)!=-1:
                        ok=True
                        ans += min(r_min,r_max) - l+1
                else:
                    ans+=min(r_min,r_max)- l+1

                    if nums[i]==minK:
                        if minK==maxK:
                            ans+=i-r_max
                            r_max=i
                        elif min(r_min,r_max)==r_min:
                            ans+=r_max-r_min
                        r_min=i
                    elif nums[i]==maxK:
                        if min(r_min,r_max)==r_max:
                            ans+=r_min-r_max
                        r_max=i                   
            cnt+=1    
        
        return ans          
            
        
        
        
            