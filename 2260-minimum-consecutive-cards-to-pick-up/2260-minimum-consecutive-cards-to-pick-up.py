class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans=float('inf')
        dic={}
        n=len(cards)
        for i in range(n):
            if cards[i] in dic:
                tans = i - dic[cards[i]]+1
                ans=min(ans,tans)
            dic[cards[i]]=i
        return ans if ans!=float('inf') else -1
            
                