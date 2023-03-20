class Solution(object):
    def leftRigthDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # get5 leftsum
        # get rightsum
        # get leftsum - rightsum
        # append everything
        # return difference

        # get left suum


        rightSum = []
        totalSum = 0
        for i in range(len(nums)-1,-1,-1):
            rightSum.insert(0,totalSum)
            totalSum += nums[i]
            print(rightSum)


      
        res = []
        totalSum = 0
        for i in range(len(nums)):
            res.append(abs(totalSum - rightSum[i]))
            totalSum += nums[i]

        return res
        


obj = Solution()
nums = [10,4,8,3]
res = obj.leftRigthDifference(nums)


print(res)