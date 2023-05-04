class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        n = len(player1)
        score1 = 0
        score2 = 0
        
        ok=0
        for num in player1:
            if ok:
                score1+=2*num
                ok-=1
            else:
                score1+=num
            if num==10:
                ok=2
        
        ok=0
        for num in player2:
            if ok:
                score2+=2*num
                ok-=1
            else:
                score2+=num
            if num==10:
                ok=2
                
        if score1 > score2:
            return 1
        elif score2 > score1:
            return 2
        else:
            return 0







        





