class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not self.isAlphanumeric(s[l]):
                l += 1
            while l < r and not self.isAlphanumeric(s[r]):
                r -= 1
            if s[l].lower() == s[r].lower():
                r -=1
                l += 1
            else:
                return False
        return True




    def isAlphanumeric(self,c):
        return (ord(\z\) >= ord(c) >= ord('a') or ord(\Z\) >= ord(c) >= ord('A') or ord(\9\) >= ord(c) >= ord(\0\))
    