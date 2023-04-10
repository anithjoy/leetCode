class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1]* len(nums)

        # prefix
        #   intializing prefix value and saving it to res

        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]


        # postfix
        #   initializing postfix value and saving it to res
        # travaling in reverse order

        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]


        return res

        
     

obj = Solution()
nums = [1,2,3,4]
# nums = [-1,1,0,-3,3]

res = obj.productExceptSelf(nums)
print(res)         