class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        n=len(transactions)
        
        mat = []
        result = []
        added=set()
        for i in range(n):
            mat.append(transactions[i].split(",") )
            if int(mat[i][2])>1000:
                result.append(transactions[i])
                added.add(i)
        
        for i in range(n-1):
            for j in range(i+1,n):
                if abs(int(mat[i][1]) - int(mat[j][1])) <= 60 and mat[i][0]==mat[j][0] and mat[i][3]!=mat[j][3]:
                    if i not in added:
                        result.append(transactions[i])
                        added.add(i)
                        
                    if j not in added:
                        result.append(transactions[j])
                        added.add(j)
        return result
                    