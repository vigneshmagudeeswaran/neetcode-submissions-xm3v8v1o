class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """ let me think 
        so let me create array called result with lenght of nums list 
        filled with 1

        then I can assign first product value as 1 and and assign it to 
        result first index
        before starting the next iteration I can reassign prefix with result[i]
        with prefix so we can get the next iteration value.

        do the same procees in reverse with suffix value"""

        res = [1] * (len(nums))

        postfix =1
        for i in range(len(nums)):
            res[i] = postfix
            postfix*=nums[i]
        suffix =1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= suffix
            suffix*=nums[i]

        return res




