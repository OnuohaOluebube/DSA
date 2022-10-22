class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums) 
        
        prefix = 1
        postfix = 1
        
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
            
        for k in range(len(nums) -1, -1, -1):
            res[k] *= postfix
            postfix *= nums[k]
            
        return res
            
            
        
        