/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    
    let map = {}
    for (let i = 0; i < nums.length; i++){
        if(nums[i] in map){
           map[nums[i]]++
        } else {
            map[nums[i]] = 1
        }
        
}
    for(let key in map)
    if(map[key] === 1) return Number(key)

};