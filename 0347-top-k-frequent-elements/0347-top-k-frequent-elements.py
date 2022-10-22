class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        arr =[[] for num in range(len(nums) +1)]
        print(arr)
        ans= []
        
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for i in count:
            arr[count[i]].append(i)
            
        for i in range(len(arr) -1,0,-1):
            for a in arr[i]:
           
                ans.append(a)
                if len(ans) == k:

                    return ans
            
         
            
        
        
        