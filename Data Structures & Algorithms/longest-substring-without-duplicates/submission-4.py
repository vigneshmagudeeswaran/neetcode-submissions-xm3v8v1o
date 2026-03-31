class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        zxyzxyz
        solution1:
            initializing:
            without_repeat =""
            longest=0
            i can dothis way
            let me create one variable(without_repeat) to store the non repating string
            i start wit empty string
            then I will loop the original string and I will append the chanracter
            if it's not exist in without_repeat(string)
            i will append it to without_repeat(string)
            else I will find max between already existing long and lenght of without_repeat
            and reassign without_repeat with the character in loop

        """
        # without_repeat =""
        # longest=0
        # for char in s:
        #     if char not in without_repeat:
        #          without_repeat +=char
        #     else:
        #         longest = max(longest,len(without_repeat))
        #         without_repeat=char
        # return longest

        l,r=0, len(s)-1 if len(s) else 0
        longest =0
        without_repeat =""
        while l<len(s):
            if s[l] not in without_repeat:
                without_repeat +=s[l]
                longest= max(longest,len(without_repeat))
                l+=1
            else:
                idx = without_repeat.index(s[l])
                without_repeat = without_repeat[idx + 1:] + s[l]
                l+=1
        return longest


            






