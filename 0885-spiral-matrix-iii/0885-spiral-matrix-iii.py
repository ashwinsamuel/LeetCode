class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        def in_bounds(i,j,r,c):
            if 0<=i<r and 0<=j<c: return True
            return False
        
        right=True
        down=True
        r,c=rStart,cStart
        ans=[[r,c]]
        if rows*cols==1: return ans
        lrbound,udbound = 1,1
        while True:
            
            #left/right
            diff = 1 if right else -1
            for i in range(lrbound):
                c+=diff
                if in_bounds(r,c,rows,cols):
                    ans.append([r,c])
                    if len(ans) == rows*cols: return ans
            right^=True
            lrbound+=1
            
            #up/down
            diff = 1 if down else -1
            for i in range(udbound):
                r+=diff
                if in_bounds(r,c,rows,cols):
                    ans.append([r,c])
                    if len(ans) == rows*cols: return ans
            down^=True
            udbound+=1
                
        