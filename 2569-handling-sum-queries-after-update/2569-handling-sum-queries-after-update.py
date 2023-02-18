class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        
        n = len(nums1)
        num1 = int( "".join(str(num) for num in nums1) ,2)
        init = 1<<n
        
        ans = []
        

        tsum=sum(nums2)
        for q,l,r in queries:
            if q==1:
                n1 = (init>>l) - 1
                n2 = (init>>r+1) - 1
                num1 ^= n1^n2
            elif q==2:
                count = num1.bit_count()
                tsum += l*count
            else:
                ans.append(tsum)

        return ans