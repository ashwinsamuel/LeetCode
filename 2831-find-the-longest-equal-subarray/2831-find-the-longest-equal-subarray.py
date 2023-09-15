class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        idxs = defaultdict(list)
        for i in range(n):
            idxs[nums[i]].append(i)
        
        print(idxs)
        '''
        diffs={}
        for key,v in idxs.items():
            nn= len(idxs[key])
            diffs[key]=[]
            for i in range(nn-1):
                diffs[key].append( idxs[key][i+1] - idxs[key][i] - 1)
        '''
        
        #print(diffs)
        
        ans=1
        for key,v in idxs.items():
            nn = len(idxs[key])
            cost=0
            l=r=0
            while r+1<nn:
                diff = idxs[key][r+1] - idxs[key][r] - 1
                r+=1
                cost+=diff
                if cost>k:
                    diff2 = idxs[key][l+1] - idxs[key][l] - 1
                    l+=1
                    cost-=diff2
                else:
                    ans=max(ans,r-l+1)

        return ans
            