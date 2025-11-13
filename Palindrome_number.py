class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        # if x is a nefative number, it cannot be a palindrome so we return False.
        string_integer = str(x)
        # We conver x to string to be able to access each digit.
        list1 = [int(digit) for digit in string_integer]
        # We create a list of integers from the string representation of x.
        length = len(string_integer)-1
        left = 0
        right = length
        palindrome = True
        # We use two pointers to compare digits from both ends of the list.
        while left <= right:
            # While the left pointer is less than or equal to the right pointer, we compare the digits.
            if list1[left] != list1[right]:
                palindrome = False
                break
            # If the digits at the left and right pointers are not equal, we set palindrome to False and break the loop.
            else:
                left += 1
                right -= 1
            # If the digits are equal, we move the pointers closer to the center.
        
        return palindrome