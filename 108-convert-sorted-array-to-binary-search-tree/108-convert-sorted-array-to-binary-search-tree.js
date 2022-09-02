/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} nums
 * @return {TreeNode}
 */
var sortedArrayToBST = function(nums) {
return BST (0, nums.length -1 )
    
    function BST(left, right){
        if (left > right) return null
        if (left === right) return new TreeNode(nums[left])
        
        const mid = Math.floor((right - left)/2) + left
        let root = new TreeNode(nums[mid])
        
        root.left = BST(left, mid-1)
         root.right = BST(mid+1, right)
        
        return root
    } 
    };