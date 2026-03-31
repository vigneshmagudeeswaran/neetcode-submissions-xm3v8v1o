class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openToClose= {')':'(','}':'{',']':'['}
        for c in s:
            if c in openToClose:
                if stack and openToClose[c] == stack[-1]:
                    stack.pop()
                    continue
                else:
                    return False
            stack.append(c)
        return not stack
        