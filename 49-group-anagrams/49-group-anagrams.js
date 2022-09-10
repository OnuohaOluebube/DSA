/**
 * @param {string[]} strs
 * @return {string[][]}
 */

    const CODES = {
        "a":0,
        "b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25,
    }
 var groupAnagrams = function(strs) {
    

const map = {}
  for(let str of strs){
const hash = hashWord(str)
if(!(hash in map)){
    map[hash] = []
}
   
          map[hash].push(str)
    }    
      
      const groups = []
      for(let key in map){
groups.push(map[key])
      
  
  }
     
     return groups
 }    
   function hashWord(str){
    const hash = new Array(26).fill(0)
    
    for(let ch of str){
        ++hash[CODES[ch]]
    } 
       
       return hash.toString()
};


  
 


