class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []

        while nums :
            a = max(nums)
            b = min(nums)

            nums.remove(a)
            nums.remove(b)

            avg = (a+b)/2

            res.append(avg)

        
        res.sort()
        # print(res)
        i = 0
        while i < len(res) and len(res) > 1:
            
            if res[i-1] == res[i]:
                res.remove(res[i])
                continue 

            i += 1

        
        return len(res)


obj1 = Solution()

nums = [4,1,4,0,3,5]
nums = [1,100]
nums = [9,5,7,8,7,9,8,2,0,7]

ans = obj1.distinctAverages(nums)

print(ans)