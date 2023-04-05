class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        
        dic={}
        for i in range(26):
            dic[chr(i+ord('a'))] = i+1
        for ch,cost in zip(chars,vals):
            dic[ch]=cost
        
        n=len(s)
        curr = dic[s[0]]
        ans= max(curr,0)
        for i in range(1,n):
            curr=max(dic[s[i]],curr+dic[s[i]])
            ans=max(ans,curr)
        
        return ans