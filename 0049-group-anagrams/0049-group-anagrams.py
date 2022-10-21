class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
       
        ans = collections.defaultdict(list)
        
     
        for str in strs:
            arr = [0] * 26
            for s in str:
                arr[ord(s) - ord("a")] += 1
                
            ans[tuple(arr)].append(str)
            
        return ans.values()
                
        
                