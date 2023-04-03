class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort(reverse=True)
        result = [[]]

        for num in nums:
            added = False
            for row in result:
                if num not in row:
                    row.append(num)
                    added = True
                    break
            if not added:
                result.append([num])

        return result