class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        h = [-g for g in gifts]
        heapify(h)

        for i in range(k):
            val = heappop(h)
            val = int(math.sqrt(-val))
            heappush(h,-val)
            
        return -sum(h)
            