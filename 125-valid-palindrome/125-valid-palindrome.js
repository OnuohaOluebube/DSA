/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    
if (!s.length) return true
    
    s = s.toLowerCase()
    
  return isValid(s)
}
    
    function isValid(s){
        let l = 0;
        let r = s.length - 1
        
        while(l < r){
            while((l < r) && isAlphaNumeric(s[l])) l++
             while((l < r) && isAlphaNumeric(s[r])) r--
            
            let isSame = (s[l] === s[r])
            if(!isSame) return false
            
            
            l++
            r--
        }
        return true
    }
    


const isAlphaNumeric = (char) => {

    const isNonAlpha = char < 'a' || 'z' < char;    // a(97) - z(122)
    const isNonNumeric = char < '0' || '9' < char;  // 0(48) - 9(57)

    return (isNonAlpha && isNonNumeric);
};
  
    
