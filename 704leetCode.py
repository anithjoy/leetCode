class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        low = 0
       
        high = len(nums) - 1

        while low <= high :

            mid = (high + low) // 2

            if target < nums[mid]:
                high = mid - 1

            elif target > nums[mid]:
                low = mid + 1

            else :
                return mid

        return -1


obj = Solution()

nums = [-1,0,3,5,9,12]
nums = [1,3,5,7] 

target = -2


ans = obj.search(nums,target)

print(ans)
            