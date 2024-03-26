class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob1(num):
            if not num:
                return 0
            elif len(num) == 1:
                return num[0]
            else:
                dp = [num[0] , max(num[0],num[1])]
                for i in range(2,len(num)):
                    dp.append(max( dp[i-2]+num[i] , dp[i-1] ))
                
                return dp[len(num)-1]
        
        if len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums[0],nums[1])
        else:
            return max(nums[0]+rob1( nums[2:-1]) , rob1(nums[1:]) )