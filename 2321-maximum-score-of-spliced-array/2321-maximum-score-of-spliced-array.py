class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        #score = sum2 + (change_1 - change_2)
        
        diff1,diff2=[],[]
        for num1,num2 in zip(nums1,nums2):
            diff1.append(num1-num2)
            diff2.append(num2-num1)
            
        max1,curr1,max2,curr2=0,0,0,0
        for d1,d2 in zip(diff1,diff2):
            curr1=max(d1,curr1+d1)
            max1=max(max1,curr1)
            
            curr2=max(d2,curr2+d2)
            max2=max(max2,curr2)
        
        return max(sum(nums2)+max1 , sum(nums1)+max2)
        
        
        