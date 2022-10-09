class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s
        
        row_map = {row:"" for row in range(1,numRows+1)}
        
        row = 1
        change = 1
        for letter in s:
            row_map[row] += letter
            
            if row == 1:
                change = 1
            if row == numRows:
                change = -1
                
            row+=change
        
        str = ""
        for row in range(1,numRows+1):
            str += row_map[row]
        
        return str