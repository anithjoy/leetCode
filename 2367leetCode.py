#2367 leetCode

class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """

        p1 = 0
        p2 = 1
        p3 = 2
       

        # for final output
        output = 0

        while p1 < len(nums)-2 and p2 < len(nums)-1 and p3 <= len(nums)-1:

            if nums[p2] - nums[p1] == diff :               
                if nums[p3] - nums [p2]  == diff : 
                    output += 1
                    p1 += 1
                    p2 = p1 + 1
                    p3 = p2 +1
                  
                elif nums[p3] - nums[p2] < diff :
                    p3 += 1
                elif nums[p3] - nums[p2] > diff :                    
                    p1 += 1
                    p2 = p1 + 1
                    p3 = p2 +1

            elif nums[p2] - nums[p1] > diff :               
                p1 += 1
                p2 = p1 + 1
                p3 = p2 + 1

            elif nums[p2] - nums[p1] < diff :               
                p2 += 1
                p3 += 1
              
        return output
        

obj1 = Solution()

nums = [4,5,6,7,8,9]
diff = 2

ans = obj1.arithmeticTriplets(nums, diff)

print(ans)

