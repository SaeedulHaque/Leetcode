class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        i=0
        while i < n: # cant use for beacuse starts index from 1, while makes sure i stays within n
            if nums[i]==val: #if same
                nums[i]=nums[n-1] #replace with last
                n=n-1 #move second pointer to left
            else:
                i=i+1 #move first pointer to right if value not there
        return n



