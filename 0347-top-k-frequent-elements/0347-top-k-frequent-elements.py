from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        
        ans = sorted(cnt.items() , key=lambda x:x[1] , reverse=True)

        result=[]
        for i in range(k):
            result.append(ans[i][0])
        return result