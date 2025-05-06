class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        i = 0
        res = []

        while i < len(words):
            j = i + 1
            len_word = len(words[i])
            while j < len(words) and len_word + 1 + len(words[j]) <= maxWidth:
                len_word += ( 1 + len(words[j]))
                j += 1
            

            word_len = j-i
            line = \\
            if j == len(words) or word_len == 1:
                line = \ \.join(words[i:j])
                line += \ \ *(maxWidth - len(line) )


            else:
                total_spaces = maxWidth - sum(len(word) for word in words[i:j])
                equal_spaces =  total_spaces // (word_len - 1)
                extra_spaces =  total_spaces  % (word_len - 1
)
                for k in range(i, j -1):
                    line += words[k]
                    spaces = equal_spaces + (1 if k - i < extra_spaces else 0 )
                    line += \ \ * spaces
                line += words[j - 1]

            res.append(line)
            i = j
        return res

            
            
             






        