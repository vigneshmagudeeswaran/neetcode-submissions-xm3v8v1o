class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        anag1= dict()
        anag2= dict()
        for i in range(len(s)):
            anag1[s[i]]= anag1.get(s[i],0) + 1
            anag2[t[i]]= anag2.get(t[i],0) + 1
        print(anag1,anag2)
        return anag1 == anag2
        