/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
const numSet = new Set()

for( let i of nums){
    
    if(numSet.has(i)) return true
    
    numSet.add(i)
    
   
}
    return false

};