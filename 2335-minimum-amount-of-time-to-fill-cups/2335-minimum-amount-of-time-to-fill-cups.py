class Solution:
    def fillCups(self, amount: List[int]) -> int:
        ans=0
        while True:
            amount.sort(reverse=True)
            
            if amount[0]>0 and amount[1]>0:
                amount[0]-=1
                amount[1]-=1
                ans+=1
            else:
                return amount[0]+ans