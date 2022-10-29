class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        
        for i,n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            
            l,r = i + 1,len(nums)-1 
            while l < r:
                sum = n + nums[l] + nums[r]
                if sum > 0:
                    r-=1
                elif sum < 0:
                    l +=1
                else:
                    res.append([n, nums[l], nums[r]])
                    l +=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
        return res
                    
            
                    
                
                
                