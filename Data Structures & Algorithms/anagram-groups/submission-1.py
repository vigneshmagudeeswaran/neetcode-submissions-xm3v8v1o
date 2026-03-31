class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashMap = defaultdict(list)
        for string in strs:
            ord_repr = [0]*26
            for c in string:
                ord_repr[ord(c)-ord('a')]+=1
            hashMap[tuple(ord_repr)].append(string)

        return hashMap.values()
        

