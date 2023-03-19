from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        nums=[nums1[i]-nums2[i] for i in range(len(nums1))]
        l=SortedList()
        ans=0
        for num in nums:
            cnt = bisect.bisect_right(l,num+diff)
            ans+=cnt
            l.add(num)
        return ans