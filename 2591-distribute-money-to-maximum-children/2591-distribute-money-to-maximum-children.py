class Solution:
    def distMoney(self, money: int, children: int) -> int:
        def is_div_possible(money,children,ans):
            if money-8*ans<children-ans: return False
            if money-8*ans>0 and children-ans==0: return False
            if money-8*ans==4 and children-ans==1: return False
            return True
        
        div=money//8
        ans=min(children,div)
        
        while ans>=0:
            if is_div_possible(money,children,ans):
                return ans
            ans-=1
        return ans
            
