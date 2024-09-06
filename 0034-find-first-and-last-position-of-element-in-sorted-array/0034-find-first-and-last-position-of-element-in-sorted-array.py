class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=self.binsearch(nums,target,True)
        right=self.binsearch(nums,target,False)

        return[left,right]
    def binsearch(self, nums, target, is_left):
        n=len(nums)
        l=0
        r=n-1
        idx=-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>target: #target 6 but mid 8 so set mid value as right 
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
            else: 
                idx=mid
                if is_left:
                    r=mid-1
                else:
                    l=mid+1
        return idx

        

            
                
            