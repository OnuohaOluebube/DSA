class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        newSet = set()
        l = 0
        m = 0
   
        for i in s:
            while i in newSet:
                m = max(m,(len(newSet)))
                newSet.remove(s[l])
                l+=1
            newSet.add(i)
            m = max(m,(len(newSet)))

        return m
                