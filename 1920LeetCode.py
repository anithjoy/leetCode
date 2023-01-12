# 1920Leetcode

"""Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive)."""


class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res = []

        if nums is None or len(nums) == 0:
            return res

        
        for i in range(len(nums)):
            res.append(nums[nums[i]])
            
        return res

nums = [0,2,1,5,3,4]
nums = [5,0,1,2,3,4]

#Imstantiate 

object1 = Solution()

ans = object1.buildArray(nums)

print(ans)
