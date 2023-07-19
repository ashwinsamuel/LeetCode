class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:

        if len(nums) == 1    : return True          # <-- some edge cases
        if 1 in nums         : return False         #

        nums = sorted(set(nums), reverse = True)    # <-- sort (big to little) and  
        if (n:=len(nums))==1 : return True          #     deal with another edge case

        for i in range(n-1):                        # <-- nums[i] >= nums[j]
            for j in range(i+1,n):
            
                if gcd(nums[i],nums[j])-1:          # <-- i,j traversal exists; 
                    nums[j]*= nums[i]               # <-- if an i,k traversal exists   
                    break                           #     (for some index k), then now 
                                                    #     a j,k traversal exists

            else: return False                      # <-- no match means no traversal 

        return True 