class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        def score(s1,s2):
            
            if s1 in s2:
                return s2
            if s2 in s1:
                return s1
            
            n1,n2=len(s1),len(s2)
            
            if n1>n2:
                i=n1-n2
            else:
                i=0
                
            while i<n1:
                ok=True
                for j in range(n2):
                    if i+j>=n1:
                        break
                    if s2[j]!=s1[i+j]:
                        ok=False
                        break
                if ok:
                    return s1[:i] + s2 #maybe max
                i+=1
            
            return s1+s2
        
        
        
        #backtracking permutations
        def permutation(lst):
            if len(lst) == 0:
                return []

            if len(lst) == 1:
                return [lst]

            l = []

            for i in range(len(lst)):
                m = lst[i]

                remLst = lst[:i] + lst[i+1:]

                for p in permutation(remLst):
                    l.append([m] + p)
            return l
        
        
        
        main = list("abc")
        mp = {
            'a':a,
            'b':b,
            'c':c
        }
        ans=""
        for p in permutation(main):
            one,two,three = p
            
            tans = score(score(mp[one],mp[two]) , score(mp[two],mp[three]))
            if ans =="" or len(tans) < len(ans):
                ans=tans
            elif len(tans) == len(ans) and tans<ans:
                ans=tans
        return ans
            
            
            
        '''
        if "aa"=="aaa":
            return "ok"
        else:
            return 'not ok'
        '''
        