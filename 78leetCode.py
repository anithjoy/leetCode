class Solution:
    def subsets(self, nums) :
        
        res = []
        subset = []

        def dfs(index):

            # base condition
            if index >= len(nums):
                res.append(subset.copy())
                return

            # add nums[i]
            subset.append(nums[index])
            dfs(index + 1)

            # add []
            subset.pop()
            dfs(index + 1)

        dfs(0)
        return res

        
a = Solution()
print(a.subsets([1,2,2]))