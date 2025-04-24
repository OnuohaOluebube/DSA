/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    
    let result = 0
    let map = {
        I : 1,
        IV : 4,
        V : 5,
        IX : 9,
        X : 10,
         XL : 40,
        L : 50,
        XC : 90,
        C: 100,
        CD :400,
        D : 500,
        CM : 900,
        M : 1000
    }
let i = 0;
    while(i < s.length){
        if(s[i] + s[i+1] in map){
            result += map[s[i] + s[i+1]]
            i+=2
           }else{
           result += map[s[i]]
        i++
          }

    }  
        
    return result
        
    }
     