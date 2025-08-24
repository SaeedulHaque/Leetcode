class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # answer = []


        # for i in range (len(nums)):
        #     product = 1                     #re initialize the product
        #     for j in range (len(nums)):
        #         if i==j:                                #skip if same
        #             pass
        #         else:
        #             product = product * nums[j]     #update the product each time
        #     answer.append(product)                  #push the final update

        # return answer


#For each element, the product except itself = (product of all elements to the left) × (product of all elements to the right)


#prefix and sufix method 

        #nums = [a, b, c, d], the product for c would be (a × b) × (d)


        n = len(nums)

        answer = [1]*n

        left_product=1              #left:      [1,    1,    1×2,  1×2×3]
        right_product=1             #right:     [2×3×4, 3×4,  4,    1]
        

        for i in range (n):
            answer[i] = left_product
            left_product = left_product*nums[i]

        for i in range (n-1, -1, -1):
            answer[i] = answer[i]* right_product
            right_product = right_product*nums[i]

        return answer               #result:    [left[i] * right[i] for each i]
