class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        '''
        __ __ __
        0
        1
        2           
                        0           1       .....
        (tsum,3) = (tsum,2) + (tsum-1,2) + .... + (tsum-9,2)
        
        
        algo:

        for tsum in range(min_sum,max_sum+1)
            base:
            5 is 1st num. so fill acc to that
        
            1 digit -> 22 digits
                10 times for 10 diff digit
                
        O(220*400)
        '''
        
        
        '''
        base:
        <= 15
        d = digits(15)
        lowest = 10
        
        __
        '''
        
        
        def count_digits(num):
            ans=0
            while num>0:
                ans+=1
                num//=10
            return ans
        
        def restrict_nums(tsum,dig,dp,maxnum):
            '''
            4546
            __ __ __ __
            0 :all
            1 :546
            '''
            if tsum<0: return 0
            if tsum==0: return 1
            if dig==1:
                if tsum<=int(maxnum[0]): return 1
                else: return 0
            if dig==0: return 0
            
            
            ans=0
            if len(maxnum)==0: print(dig)
            for num in range(int(maxnum[0])):
                ans = (ans + count_nums(tsum-num,dig-1,dp) ) % MOD
            ans = (ans + restrict_nums(tsum-int(maxnum[0]),dig-1,dp,maxnum[1:]) ) % MOD
            return ans
        
        def count_nums(tsum,dig,dp):
            
            if tsum==0:
                dp[(tsum,dig)]=1
                return 1
            elif tsum<0:
                dp[(tsum,dig)]=0
                return 0
            if dig==1:
                if 0<tsum<=9:
                    dp[(tsum,dig)]=1
                    return 1
                else:
                    dp[(tsum,dig)]=0
                    return 0
                
            
            if (tsum,dig) in dp:
                return dp[(tsum,dig)]

            ans=0
            for num in range(10):
                ans= (ans + count_nums(tsum-num,dig-1,dp) ) % MOD
            dp[(tsum,dig)]=ans

            return ans
        
        dp={}
        ans=0
        MOD = 10**9+7
        
        for tsum in range(min_sum,max_sum+1):
            d = count_digits(int(num2))
            ans2 = restrict_nums(tsum, d ,dp,num2)
            
            d = count_digits(int(num1)-1)
            ans1 = restrict_nums(tsum, d ,dp,str(int(num1)-1))
            ans += (ans2-ans1)%MOD
            #print(ans1,ans2,tsum)
        '''
        for k,v in dp.items():
            print(k,v)
        '''
        
        return ans%MOD
            
                    
            
            
            
            