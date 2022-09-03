/**
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function(rowIndex) {
     if (rowIndex === null) return []
    
        let pascal = [[1]]

        for(let i = 1;i <= rowIndex;i++) {
            pascal[i] = [];
            for(var j = 0; j < i + 1;j++) {
                pascal[i][j] = (pascal[i - 1][j] || 0) + (pascal[i - 1][j - 1] || 0);
            }
        }
            
        return pascal[rowIndex];
   
};