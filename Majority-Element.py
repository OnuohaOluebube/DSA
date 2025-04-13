class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxNo = 0
        count = 0
        for n in nums:
            if count == 0:
                maxNo = n
            count += (1 if maxNo == n else -1)
        return maxNo

            


        