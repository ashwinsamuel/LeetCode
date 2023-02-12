class Solution:
    def minPartitions(self, n: str) -> int:
        
        ans = "0"
        for ch in n:
            if ch > ans:
                ans = ch
                if ch == "9":
                    return 9
        
        return int(ans)