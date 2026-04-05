class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        # heapq.heappush(minHeap)
        if self.large and num > self.large[0]:
             heapq.heappush(self.large,num)
        else:
            heapq.heappush(self.small,-1* num)
        if len(self.large) > len(self.small)+1:
            value = heapq.heappop(self.large)
            heapq.heappush(self.small,-1*value)
        if len(self.large)+1 < len(self.small):
            value = heapq.heappop(self.small)
            heapq.heappush(self.large,-1*value)


        

        

    def findMedian(self) -> float:
        #print(f'minHeap:{self.minHeap},maxHeap:{self.maxHeap}')
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        if len(self.small) < len(self.large):
            return self.large[0]
        if len(self.small) == len(self.large) and self.small:
            return ((self.small[0] * -1 ) + (self.large[0]))/2



        
        