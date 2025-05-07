class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = match = 0

        while i < len(t) and j < len(s):
            if s[j] == t[i]:
                j += 1
                i += 1
                match += 1
            else:
                i += 1
        return match == len(s)
            
            

        