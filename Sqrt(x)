# Suppose x = 9.
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= x:
            mid = (left + right)//2
            # The value of mid will be mid=4.5, this will be rounded down to mid=4 due to double slashes.
            if mid*mid > x:
                right -= 1
                # As 4*4 > 9, we will move the right pointer to 3(mid - 1).
                # Since right=3 now, we will again start from the top getting the value mid= 1.
            elif mid*mid < x:
                left += 1
                # Since the new value of mid is 1 and mid*mid < x, we will move the left pointer to mid + 1 which is 2.
                # After repeating this process with left = 2 and right = 3, we get mid = 2 which is still less than x so the left pointer now moves to left=3.
            else:
                return mid
                # left=3 and right=3 gives mid=3. Since now mid*mid = x, we return mid as it is neither less than nor greater than x.
        return right
        # We return right instead 0f left because when the loop ends, left will be at a position greater than the actual square root>
        # Since we need to round down, we return right which will be at the floored position of the square root.
