class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        n=len(gas)
        diff = [gas[i]-cost[i] for i in range(n)]
        
        total,curr=0,0
        idx=0
        for i in range(n):
            total += diff[i]
            curr += diff[i]
            if curr < 0:
                idx=i+1
                curr=0
        
        return idx if total>=0 else -1