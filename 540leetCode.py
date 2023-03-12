class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(0,len(nums)-1,2):
            if nums[i] != nums[i+1]:
                return nums[i]
            
        return nums[-1] 



obj = Solution()
nums = [1,1,2,3,3,4,4,8,8]
ans = obj.singleNonDuplicate(nums)
print(ans)