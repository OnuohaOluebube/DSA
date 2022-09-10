/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
        let map = {};
    let res = [];
    let bucket = Array.from({ length: nums.length + 1 }, ()=>[]);
    
    for (let n of nums){
       n in map ? ( map[n] +=1): map[n]=1
    }
for (let c in map){
    bucket[map[c]].push(c)
}
    
      for (let i = bucket.length - 1; i >= 0; i--) {
        if (bucket[i].length > 0) {
            bucket[i].forEach((elem)=> res.push(elem));
            if(k == res.length){
                return res;
            }
        }
    }
    
    
    
    console.log(bucket)
};