class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums) #takes the number of elements inside the array to run the loop till
        hmap={} #empty hashmap
        for i in range (n):
            diff=target-nums[i] #difference between target and the i'th number in the array
            if diff in hmap: #if there exists the difference value which is requierd to reach the target value
                return [hmap[diff],i] #return the "indexes" of the numbers inside the array
            hmap[nums[i]]=i #if the difference is not found then change the index (move up by 1 or i)
        return [] #return empty if not found
        