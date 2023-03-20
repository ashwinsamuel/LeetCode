class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        ans=0
        done=set()
        for num in nums:
            i=0
            while i<32:
                if 1<<i==num:
                    done.add(i)
                    if i==ans:
                        j=i+1
                        while j<32:
                            if j not in done:
                                ans=j
                                break
                            j+=1
                    break
                i+=1
        print(done)
        return 1<<ans