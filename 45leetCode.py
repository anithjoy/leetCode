# not completed
class Solution(object):
    def jump(self, nums):
        
        
        {# """
        # :type nums: List[int]
        # :rtype: int
        # """
        # # we are at nums[0]

        
        # i = 0
        # jump = 0
        # while i < len(nums)-1:
        #     value = nums[i]
            
            
        #     start = i
        #     end = value
        #     if i+ value < len(nums)-1:
        #         greaterNumber = max(nums[start+1:end+1])
        #         i = nums.index(greaterNumber,start+1,end+1)
        #         jump += 1
        #     else:
        #         jump += 1
        #         break

        # return jump
        }
        
        {        
     # i = 0  #list pointer
        # jumps = 0 #number of jumps
        # maxJump = 0
        # while (i<len(nums)-1):
        #     # value = nums[i]
        #     if(len(nums)== 1):
        #             return jumps
        
        #     if i+ nums[i] < len(nums):
        #         if (i + nums[i]) == (len(nums)-1):
        #             jumps += 1
        #             return jumps
        #         else:
        #             maxJump = max(nums[i+1:nums[i]+i+1])
        #             if (maxJump == nums[nums[i]+i]):
        #                 i = nums[i]+1
        #                 jumps += 1
        #             else:
        #                 i = nums.index(maxJump,i+1,nums[i]+i+1)
        #                 jumps += 1

        #     else:
        #         jumps += 1
        #         return jumps
        }
        
        res = 0
        l = r = 0

        while(r<len(nums)-1):
            farthest = 0
            for i in range(l,r+1):
                farthest = max(farthest,i + nums[i])
            l = r+1
            r = farthest
            res += 1
        return res


                    


            

"""New plannine -
-will get list of nums . there will be a pointer in the list
-we will take the value of the pointer
- current-pointer-position + value-of-pointer <= len(list)
if the above condition is true, we will take the maximum of the pointer and check all the value inside that range and will choose maximum of that pointer to react at the base """

obj = Solution()
ans = obj.jump([2,3,1,1,4])
# ans = obj.jump([0])
# ans = obj.jump([1])
# ans = obj.jump([1,1,1,1,1])  
# ans = obj.jump([1,2,1,1,1])  
print(ans)

