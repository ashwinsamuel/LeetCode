class Solution:
    def decodeString(self, s: str) -> str:
        num=[]
        nums = []
        stck = []
        for ch in s:
            if ord('0')<=ord(ch)<=ord('9'):
                num.append(ch)
            elif ch == '[':
                nums.append(int("".join(num)))
                num=[]
                stck.append(ch)
            elif ch == ']':
                tstr=deque()
                while stck[-1]!='[':
                    tstr.appendleft(stck.pop())
                stck.pop()
                tstr = "".join(tstr)
                
                n = nums.pop()
                for j in range(n):
                    stck.append(tstr)
            else:
                stck.append(ch)
        return "".join(stck)