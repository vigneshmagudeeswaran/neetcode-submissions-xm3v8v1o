class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            a= list(s)
            a.sort()
            b= list(t)
            b.sort()
            if a==b:
                return True
            else:
                return False
        return False
