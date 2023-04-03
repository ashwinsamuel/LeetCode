class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [[]]
        prev=0
        for num in nums:
            if prev!=num:
                row=0
                result[0].append(num)
                row+=1
                prev=num
            else:
                if row<len(result):
                    result[row].append(num)
                else:
                    result.append([num])
                row+=1
                prev=num
        return result
