class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        
        '''
        0 negatives: all
        1 neg: if len==1: ans else w/o
        even neg: all
        odd neg: remove max of negs
        '''
        
        n=len(nums)
        pos=neg=zero=0
        pos_ans = neg_ans = 1
        neg_max=-float('inf')
        
        #n = pos+neg+zero
        for num in nums:
            if num>0:
                pos+=1
                pos_ans*=num
            elif num<0:
                neg+=1
                neg_ans*=num
                neg_max=max(neg_max,num)
            else:
                zero+=1
        
        if neg%2==0:
            if neg>0:
                return pos_ans*neg_ans
            else:
                if pos==0:
                    return 0
                else:
                    return pos_ans
        else:
            if neg==1:
                if pos>0:
                    return pos_ans
                elif zero>0:
                    return 0
                else:
                    return neg_ans
            else:
                return pos_ans*neg_ans//neg_max
            
        