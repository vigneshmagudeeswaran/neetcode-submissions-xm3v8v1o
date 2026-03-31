class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap=defaultdict(list)
        max_length = 0

        for i in nums:
            if i-1 not in nums:
                j =i
                length =1
                while j+1 in nums:
                    hashmap[i].append(j+1)
                    length +=1
                    j=j+1
                max_length = max(max_length,length)
        return max_length

            

        