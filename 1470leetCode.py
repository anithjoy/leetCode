class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """

        
        newArray = []
        i = 0
        while(i<n):
            newArray.append(nums[i])
            newArray.append(nums[i+n])   
            i += 1

        return newArray
    

obj = Solution()
ans = obj.shuffle([1,2,3,4,5,6],3)
print(ans)
        