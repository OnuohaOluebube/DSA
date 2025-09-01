class MedianFinder:

    def __init__(self):
        # small = max queue,#large = min queue
        self.small, self.large = [],[]
       
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-1 * num)
        # ensure every num in small <= every num in large
        if self.small and self.large and ((-1 * self.small[0] ) > self.large[0]):
            val = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, val)

        #handle uneven length
        if len(self.small) > len(self.large )+ 1:
            val = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, val)
        elif len(self.small) + 1 < len(self.large ):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (((self.small[0] * -1) + self.large[0]) /2.0)
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()