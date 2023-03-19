class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def addall(i,j,vis,n,num):
            if n<0:          
                vis.add(num)
                return
            
            if i==n or j==n:
                addall(i,j,vis,n-1,num)
            else:
                addall(i,j,vis,n-1,num)
                num = num^(1<<n)
                addall(i,j,vis,n-1,num)
            return 
        
        mp = {i:[] for i in range(1,1001)}
        n=len(nums)
        vis=set()
        
        for i in range(n):
            mp[nums[i]].append(i)
            if (nums[i]-k) in mp:
                for j in mp[nums[i]-k]:
                    bno = (1<<i) | (1<<j)
                    addall(i,j,vis,n-1,bno)
                    #print(f'{j,i}: {vis}')
                    
            if (nums[i]+k) in mp:
                for j in mp[nums[i]+k]:
                    bno = (1<<i) | (1<<j)
                    addall(i,j,vis,n-1,bno)
                    #print(f'{j,i}: {vis}')
        return (1<<n) - len(vis) -1
                        
                