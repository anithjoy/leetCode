class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums) == 0):
            return 0
        nums = sorted(nums)

# the below code is for those array whose length is greater than 1 (a.len > 1)
        nextNum =  nums[0]+1
        count = 0
        maxCount = 0
        prev = "a"
        
        for num in  nums:
            if nextNum == num:
                count += 1
                nextNum += 1 
                prev = num
            elif prev == num:
                continue
            else:
                count = 1
                nextNum = num + 1
                prev= num

            maxCount= max(maxCount,count)

        return maxCount



obj = Solution()

nums = [100,4,200,1,3,2]
nums = []
nums = [0,3,7,2,5,8,4,6,0,1]
nums = [2]
nums = [1,2,0,1]

res = obj.longestConsecutive(nums)
print(res)