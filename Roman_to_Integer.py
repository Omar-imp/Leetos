class Solution:
    def romanToInt(self, s: str) -> int:
        i = 0
        total = 0
        total1 = 0
        x = 0

        roman = { "I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        length = len(s)

        while i < len(s)-1:
            
            if roman[s[i]] < roman[s[i+1]]:
                x = roman[s[i+1]]-roman[s[i]]
                i += 2
 
            elif roman[s[i]] >= roman[s[i+1]]:
                x = roman[s[i]] 
                i += 1
        
            total += x
    
        if roman[s[length - 1]] > roman[s[length -2]]:
            total1 = total 
        else:
            total1 = total + roman[s[length - 1]]
            
        return total1
