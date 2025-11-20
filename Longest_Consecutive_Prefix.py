class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        new_arr = ""
        
        # We find the string with minimum length in the list using for loop.
        for x in range(len(strs)-1):
            if len(strs[x]) < len(strs[x+1]):
                mint = len(strs[x])
            else:
                mint = len(strs[x+1])
        
        # We run the for loop for the length of the shortest string.
        for i in range(mint):
            # We compare each character of all strings with the first string.
            for s in strs:
                if s[i] != strs[0][i]: 
                    # if the above condition is true, we return the new_arr which contains the longest common prefix.
                    return new_arr
            # We keeo adding characters to new_arr as long as they are same in all strings.
            new_arr += strs[0][i]
        # Finally, we return the new_arr.
        return new_arr  