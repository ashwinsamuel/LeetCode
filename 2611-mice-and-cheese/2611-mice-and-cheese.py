import heapq

class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        win1,eq=0,0
        ans=0
        lst1,lst2=[],[]
        
        for i in range(n):
            if reward1[i]>reward2[i]:
                win1+=1
                ans+=reward1[i]
                lst1.append(i)
            elif reward1[i]==reward2[i]:
                eq+=1
                ans+=reward1[i]
            else:
                lst2.append(i)
                ans+=reward2[i]
        
        if win1==k:
            return ans
        
        hp=[]
        if win1<k:
            if k-win1<= eq:
                return ans
            else:
                win1+=eq
                for it in lst2:
                    val = reward2[it] - reward1[it]
                    heapq.heappush(hp,(val,it))
                
                for i in range(k-win1):
                    val,it = heapq.heappop(hp)
                    ans-=val
                
                return ans
        else:
            for it in lst1:
                val = reward1[it] - reward2[it]
                heapq.heappush(hp,(val,it))

            for i in range(win1-k):
                val,it = heapq.heappop(hp)
                ans-=val

            return ans
            