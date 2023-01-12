# 1929LeetCode

"https://leetcode.com/problems/concatenation-of-array/"

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res = []
        if not nums:
            return res
            
        for i in range((len(nums)) * 2):
            i = i % len(nums)

            res.append(nums[i])

        return res

# d8ifferent inputs
nums = [1,2,1]
nums = [1,3,2,1]

object1 = Solution()

ans = object1.getConcatenation(nums)

print(ans)
