/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
  const rows = {};
    const cols = {};
    const squares = {};
for(let r = 0; r < 9; r ++){
    for(let c = 0; c < 9; c ++){
        
        const num = board[r][c]
        
       
            if (num === '.') {
                continue;
            }

        
 const grid = `${Math.floor(r / 3)}${Math.floor(c / 3)}`;
        
        if(!rows[r]) {
            rows[r] = new Set()
        }
         if(!cols[c]) {
            cols[c] = new Set()
        }
         if(!squares[grid]) {
            squares[grid] = new Set()
        }
        
        if( rows[r].has(num) || cols[c].has(num) || squares[grid].has(num) ) 
        {
            return false
        }
       
            rows[r].add(num);
          cols[c].add(num);
            squares[grid].add(num);
    }  
}
    
    return true;

}