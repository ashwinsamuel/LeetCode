class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #minimum k s.t. sum(pile//k +1) <=h
        
        #if h==len(piles) then k=max(piles)
        n=len(piles)
        l,r=0,max(piles)
        
        while l<r:
            mid=(l+r)//2
            if mid==0: return 1
            tsum= sum(pile//mid+1 if pile%mid else pile//mid for pile in piles)
            if tsum<=h:
                r=mid
            else:
                l=mid+1
        return r