class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        mini = min(x,y)
        ans=2*(mini)
        ans+=z
        if mini == x:
            if y>mini:
                ans+=1
        else:
            if x>mini:
                ans+=1
        return 2*ans
                