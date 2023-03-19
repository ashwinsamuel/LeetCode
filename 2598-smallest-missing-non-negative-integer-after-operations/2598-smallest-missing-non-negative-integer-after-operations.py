class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mp = {}
        
        for num in nums:
            idx = num %value
            mp[idx] = mp.get(idx,0) +1
        
        print(mp)
        
        mini = float('inf')
        for i in range(value):
            if i not in mp:
                mini=0
                rem = i
                break
            if mp[i]<mini:
                mini=mp[i]
                rem=i
        return mini*value +rem