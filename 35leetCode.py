class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l = 0
        r = len(nums) - 1
        

        while l <= r :

            m = (l+r) // 2
            if nums[m] == target:
                return m

            elif nums[m] > target:
                r = m - 1

            else:
                l = m + 1

        if nums[m] < target : 
            return m + 1
        else: return m


obj = Solution()

nums = [-1,0,3,5,9,12]
nums = [1,3,5,7] 

target = 8


ans = obj.searchInsert(nums,target)

print (ans)