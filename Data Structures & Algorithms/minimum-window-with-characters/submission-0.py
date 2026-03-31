from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t =="":
            return ""
        t_frequency = {}
        for i in t:
            t_frequency[i]= t_frequency.get(i,0)+1
        window ={}
        seen,need = 0, sum(t_frequency.values())
        res = [0,0]
        resLen=float("infinity")
        l=0
        for r in range(len(s)):
            char = s[r]
            if char in t_frequency:
                window[char] = window.get(char,0)+1
                if window[char] <= t_frequency[char]:
                    seen +=1
            while seen == need:
                
                if (r-l+1)< resLen:
                    res=[l,r]
                    resLen = min(len(s[res[0]:res[1]+1]),resLen)
                
                if s[l] in window:
                    window[s[l]] -=1
                    if window[s[l]] < t_frequency[s[l]]:
                        seen -=1
                l +=1
        return s[res[0]:res[1]+1] if resLen != float("infinity") else ""





        



            





        

        