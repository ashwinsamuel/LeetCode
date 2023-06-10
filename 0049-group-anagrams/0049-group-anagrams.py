from sortedcontainers import SortedList
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mp={}
        for s in strs:
            st = sorted(s)
            st = "".join(st)
            mp[st] = mp.get(st,[]) + [s]
        
        ans=[]
        for k,v in mp.items():
            ans.append(list(v))
        
        return ans
            
        
        
            