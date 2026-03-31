class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum= 0
        l,r= 0,len(heights)-1
        while l<r:
            minimum_height = min(heights[l],heights[r])
            maximum=max(maximum,minimum_height*(r-l))
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return maximum