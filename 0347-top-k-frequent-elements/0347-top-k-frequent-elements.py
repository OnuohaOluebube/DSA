class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        arr = [[] for num in range(len(nums) +1)]
        res = []
        
        for num in nums:
            count[num] = 1+count.get(num, 0)
        for i,c in count.items():
            arr[c].append(i)
        for a in range(len(arr) -1, 0, -1):
            for i in arr[a]:
                res.append(i)
                if len(res) == k:
                    return res
            
            


            
         
            
        
        
        