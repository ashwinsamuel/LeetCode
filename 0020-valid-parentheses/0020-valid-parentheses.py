class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = set(['(','{','['])
        closed = {
            ')':'(',
            '}':'{',
            ']':'[',
        }

        for ch in s:
            if ch in open:
                stack.append(ch)
            else:
                if not stack or closed[ch] != stack.pop():
                    return False
        
        if not stack:
            return True
        else:
            return False
                    