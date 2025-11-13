class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        string_integer = str(x)
        list1 = [int(digit) for digit in string_integer]
        length = len(string_integer)-1
        left = 0
        right = length
        palindrome = True
        while left <= right:
            if list1[left] != list1[right]:
                palindrome = False
                break
            else:
                left += 1
                right -= 1
        
        return palindrome