class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        ans = []
        mp = {}
        for l in range(1,34):
            for i in range(len(s)-l+1):
                sub=s[i:i+l]
                if sub not in mp:
                    mp[sub] = i
        
        for x,y in queries:
            sub = bin(x^y)[2:]
            
            if sub in mp:
                ans.append([mp[sub],mp[sub]+len(sub)-1])
            else:
                ans.append([-1,-1])
        
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
                    
            
            
            