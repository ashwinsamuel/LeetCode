class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        min_diff = 20000
        ans = 0

        for i in range(len(nums)-2):

            if nums[i] == nums[i-1] and i>0:
                continue

            l = i + 1
            r = len(nums) - 1
            
            while l<r:

                s = nums[i] + nums[l] + nums[r]
                diff = abs(target - s)

                if diff < min_diff:
                    min_diff = diff
                    ans = s
                
                if s == target:
                    return s
                elif s < target:
                    l_prev = l
                    while nums[l_prev] == nums[l] and l<r:
                        l += 1
                else:
                    r_prev = r
                    while nums[r_prev] == nums[r] and l<r:
                        r -= 1
        
        return ans