class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            
            #find max
            max_w = 0
            max_id = 0
            for i in range(len(gifts)):
                if gifts[i] > max_w:
                    max_id = i
                    max_w = gifts[i]
            
            gifts[max_id] = math.sqrt(max_w)//1
            
        #sum
        ans = 0
        for w in gifts:
            ans += w
        
        return int(ans)
            