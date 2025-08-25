class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        out = []

        temp = 0

        for i in range (len(nums)):
            val = nums[i]*nums[i]
            out.append(val)
            val = 0

        out.sort()
        
        return out