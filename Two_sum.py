class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]ls
        """
        l = len(nums)
        #l is the length of the nums list
        for i in range(l):
           # i starts from 0 to l-1 so that we can access all elements except the last one
           for j in range(i +1, l):
                #j starts from i+1 to avoid using the same element twice
               if nums[i] + nums[j] == target:
                    return [i, j]
               # if no such pair is found in the list, we return None
        return None
