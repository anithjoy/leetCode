class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(1,len(nums),2):
            if nums[i-1]!= nums[i]:
                return nums[i-1]
        return nums[-1]


obj = Solution()
nums = [2,2,1]
nums = [4,1,2,1,2]
nums = [1]

ans = obj.singleNumber(nums)
print(ans)