# nums = [3, 2, 5, 8, 6, 0, 0, 0, 1]
# S = (3, 2, 5, 8, 6, 0, 1)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        S = set(nums)
        # S is a hashset which has the list(nums) stored within it. In this hashset, there are no duplicate values stored.
        max_len= 0
        for num in nums:
            if num - 1 not in S:
            # Line-7: Suppose num = 3, this line will check if 2(num-1) exists in the hashset. If it does, then we go back to start of the loop.
            # Now suppose num = 5. 4(num - 1) does not exist in the hashset, so we assign next_sum a value of 6(num + 1) and make the lenghth 1 as we have a value 5.
            # Now we check if next_num = (6) exists. It does in hashset so we increment the length by 1 again and add 1 to next_num.
            # next_num = 7 does not exist so our max lenght is 2 for now.
                next_num = num + 1
                curr_len = 1
                while next_num in S:
                    curr_len += 1
                    next_num += 1
                longest = max(max_len, curr_len)
        return longest
        # In the end the max_len is 4 as we have 0, 1, 2, 3 as the longest consecutive sequence in the hashset.