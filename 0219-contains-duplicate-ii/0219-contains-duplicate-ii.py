class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numSet = set()
        L = 0
        for R in range(len(nums)):
            if R - L > k:
                numSet.remove(nums[L])
                L += 1
            if nums[R] in numSet:
                return True
            numSet.add(nums[R])
        return False

        