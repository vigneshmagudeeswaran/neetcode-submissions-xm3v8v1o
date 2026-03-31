class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLength=0
        for i in nums:
            if i-1 not in nums:
                length =1
                j=i
                while (j+length) in nums:
                    length+=1
  
                maxLength = max(maxLength,length)
        return maxLength

            

        