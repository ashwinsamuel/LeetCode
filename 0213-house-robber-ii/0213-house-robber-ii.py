class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob1(num):
            if len(num) < 2:
                return num[0]
            else:
                dp = [num[0] , max(num[0],num[1])]
                for i in range(2,len(num)):
                    dp.append(max( dp[i-2]+num[i] , dp[i-1] ))
                
                return dp[len(num)-1]
        
        if len(nums)<2:
            return nums[0]
        else:
            part1 = nums[:-1]
            part2 = nums[1:]
            
            return max( rob1(part1) , rob1(part2) )