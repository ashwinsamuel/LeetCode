class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed = {
            '(':')',
            '{':'}',
            '[':']',
        }

        for ch in s:
            if ch in closed:
                stack.append(ch)
            else:
                if not stack or closed[stack.pop()] != ch:
                    return False
        
        if not stack:
            return True
        else:
            return False
                    