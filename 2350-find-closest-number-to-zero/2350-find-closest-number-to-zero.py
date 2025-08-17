class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val = nums[0]
        n=len(nums)
        for i in range(n):
            if abs(nums[i]) < abs(val):
                val = nums[i]
        print(val)
        if val<0 and abs(val) in nums:
            return abs(val)
        else:
            return val




