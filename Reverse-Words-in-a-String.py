class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        res = []
        i = n - 1

        while i >= 0:
            while i >= 0 and s[i] == \ \:
                i -= 1
            if i < 0:
                break
            j = i
            while i >= 0 and s[i] != \ \:
                i -= 1
            res.append(s[i+1:j+1])
        return \ \.join(res)


            
        