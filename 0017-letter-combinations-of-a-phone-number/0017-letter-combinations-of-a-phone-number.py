class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        result=[]
        mp = {
            2:['a','b','c'],
            3:['d','e','f'],
            4:['g','h','i'],
            5:['j','k','l'],
            6:['m','n','o'],
            7:['p','q','r','s'],
            8:['t','u','v'],
            9:['w','x','y','z']
        }
        
        def solve(tstr, i):
            
            if i==len(digits):
                result.append(tstr)
                return

            for ch in mp[ int(digits[i]) ]:
                tstr = tstr+ch
                solve(tstr,i+1)
                tstr = tstr[:-1]
            
            return
        
        if len(digits)==0:
            return []
        else:
            solve("",0)
            return result