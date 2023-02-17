class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        # iterative function for finding gcd
        def gcd(a, b):
            while a and b:
                a, b = b, a % b
            return a or b
			# Time complexity - O(log(min(a, b)) = O(log n)

        
        cnt = 0
        n = len(nums)
        
        for i in range(n):
            tmp_gcd = 0 # gcd of zero with any number is equal to the number itself
            
            for j in range(i,n):
                tmp_gcd = gcd(tmp_gcd, nums[j])
                
                

                if tmp_gcd == k:
                    cnt += 1
                elif tmp_gcd < k: # gcd cannot get bigger
                    break
        
        return cnt