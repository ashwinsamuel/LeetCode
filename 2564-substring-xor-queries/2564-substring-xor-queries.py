class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        finder = defaultdict(lambda: [-1, -1])
        for l in range(33, 0, -1):
            for i in range(len(s)-l, -1, -1):
                finder[int(s[i:i+l], 2)] = [i, i+l-1]
        ans = []
        for a, b in queries:
            ans.append(finder[a^b])
        return ans
            
        
        
        '''
        mp = {}
        for x,y in queries:
            sub = bin(x^y)[2:]
            
            if sub not in mp:
                mp[sub] = s.find(sub)

            if mp[sub] == -1:
                ans.append([-1,-1])
            else:
                ans.append([mp[sub],mp[sub]+len(sub)-1])
        ''' 
        return ans
                    
            
            
            