/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
let map = {
    ")":"(",
     "}":"{",
     "]":"[",
}

let stack = []

for (let i = 0; i<s.length; i++){
    if(s[i] === "(" || s[i] === "{" || s[i] === "[" ){
        stack.push(s[i])
    } else if (stack[stack.length -1] === map[s[i]]){
         stack.pop(s[i])
    } else {
        return false
    }
    
  
        
}
     return stack.length === 0 ?  true : false
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
//       let map = {
//         ")": "(",
//         "]": "[",
//         "}": "{"
//       }
// let arr = []
// for(let i = 0; i < s.length; i++){
//     if(s[i] === "(" || s[i] === "[" ||s[i] === "{"  ){
//         arr.push(s[i])
//     }else{
//         if(arr[arr.length - 1] === map[s[i]]){
//             arr.pop()
//         }else{return false}
//     }
// }
//     return arr.length === 0 ? true:false
};


