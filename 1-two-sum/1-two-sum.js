/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
let sum = {}
for(let i = 0; i<nums.length; i++ ){
    if(target - nums[i] in sum){
        return ([i, sum[target-nums[i]]])
    }else{
        sum[nums[i]] = i
    }
}


};