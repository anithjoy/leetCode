#1leetCode


# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         hashMap = {}
#         list = []

#         for index in range(len(nums)):
#             difference = target-nums[index]
            
#             if difference in hashMap:
#                 list.append(hashMap[difference])
#                 list.append(index)
#                 return list

#             hashMap[nums[index]]=index


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}

        for index in range(len(nums)):
            difference = target - nums[index]
            if difference in hashMap:
                return [hashMap[difference],index] #rectify this
            else:
                hashMap[nums[index]] = index


obj1 = Solution()

nums = [2,7,11,15]
target = 9
ans = obj1.twoSum(nums,target)

print(ans)
