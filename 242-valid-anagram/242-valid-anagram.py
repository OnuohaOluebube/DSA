class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        countS,countT = {},{}
        
        if len(s) != len(t):
            return False
        for n in s:
            if not n in countS:
                countS[n] = 1
            else:
                countS[n]+=1
        
        for n in t:
            if not n in countT:
                countT[n] = 1
            else:
                countT[n]+=1
                
        return countS == countT
            
            
                
            