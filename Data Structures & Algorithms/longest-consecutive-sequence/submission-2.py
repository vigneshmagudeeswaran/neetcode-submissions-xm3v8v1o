class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      
        max_length = 0

        for i in nums:
            if i-1 not in nums:
                j =i
                length =1
                while j+1 in nums:
                   
                    length +=1
                    j=j+1
                max_length = max(max_length,length)
        return max_length

            

        