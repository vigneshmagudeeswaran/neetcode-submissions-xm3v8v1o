class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 1)two pointers -one at left end one at right end
        # 2)add the values of pointers based on total shift the pointer
        left:int = 0
        right:int= len(numbers)-1
        while left<right:
            total =numbers[left]+numbers[right]
            if total==target:
                return [left+1,right+1]
            elif total < target:
                left+=1
            else:
                right-=1
