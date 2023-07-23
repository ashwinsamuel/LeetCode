class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = {}
        for i in range(n):
            if nums[i] not in freq:
                freq[nums[i]] = []
            freq[nums[i]].append(i)

        arr = [0] * n
        for k, v in freq.items():
            prev_sum = sum(v)
            n=len(v)
            counter=n
            for i, idx in enumerate(v):
                arr[idx] = prev_sum - counter*idx + (n-counter)*idx
                prev_sum -= 2*idx
                counter -= 1
                #print(prev_sum, counter)

        return arr