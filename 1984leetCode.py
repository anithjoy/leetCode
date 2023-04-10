
class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        l,r = 0, k-1
        res = float("inf")

        while r < len(nums):
            res = min(res, nums[r]-nums[l])
            l,r = l+1, r+1
        return res
    
obj = Solution()
nums = [1,4,9,7]
k = 2
ans = obj.minimumDifference(nums,k)
print(ans)