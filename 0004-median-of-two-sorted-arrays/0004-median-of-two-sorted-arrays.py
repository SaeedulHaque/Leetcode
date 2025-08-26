class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1+nums2
        n=len(nums)
        nums.sort()
        if n%2 == 0: #even
            med = (nums[n/2 - 1] + nums[n/2]) / 2.0            
        else: #odd
            med = nums[n/2]

        return med