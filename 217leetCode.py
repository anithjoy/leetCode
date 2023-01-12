"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true"""



class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashMap = {}
        for number in nums:
            if number in hashMap:
                return True
            hashMap[number]=1
        return False


obj1 = Solution()
ans = obj1.containsDuplicate([1,2,3])

print(ans)