class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        [1,2,4,6]
    pre=[1,1,2,8]
    suff=[48,24,6,1]
    answ=[48,24,12,8]
        '''
        pre= [1]* len(nums)
        suff= [1]* len(nums)
        res=[1] * len(nums)
        for i in range(1,len(nums)):
            # here we need to multiply numbers before that particular number
            pre[i] = pre[i-1] * nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            suff[i] = suff[i+1] * nums[i+1]
        
        for i in range(len(pre)):
            res[i] = pre[i] * suff[i]

        return res




        