class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count =  {}
        frequency = [[] for i in range(len(nums)+1)]
        res =[]

        for i in nums:
            count[i]=count.get(i,0)+1
        for num, count in count.items():
            frequency[count].append(num)
        for i in range(len(frequency)-1,0,-1):
            for n in frequency[i]:
                res.append(n)
            if len(res) == k:
                return res
        return res
