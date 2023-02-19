class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0: return [1]
        
        prev = [1,1]
        new=prev
        for j in range(1,rowIndex):
            new = [1]
            for i in range(len(prev)-1):
                new.append(prev[i]+prev[i+1])
            new.append(1)
            prev=new
        return new