class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        h = [-g for g in gifts]
        heapify(h)

        for i in range(k):
            heappush(h,-int(math.sqrt(-heappop(h))))
            
        return -sum(h)
            