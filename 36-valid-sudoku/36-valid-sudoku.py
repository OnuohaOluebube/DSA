class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        col = collections.defaultdict(set)
        row = collections.defaultdict(set)
        square = collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                grid = (r//3,c//3)
                          
                if (num in row[r] or num in col[c] or num in square[grid]): 
                    return False
                else:
                    row[r].add(num)
                    col[c].add(num)
                    square[grid].add(num)
                        
        return True
                        
                        
                   