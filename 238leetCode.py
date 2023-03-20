class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            sum = 1
            for j in range(len(nums)):
                if i == j :
                    # continue
                    if nums[i] != 0:
                        sum = sum/nums[i]
                    else:
                        sum = sum/1
                sum *= nums[j]
                print(sum)

            res.append(sum)


        return res

obj = Solution()
nums = [1,2,3,4]
nums = [-1,1,0,-3,3]

res = obj.productExceptSelf(nums)
print(res)         