class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums.sort()
        hashMap = {}
        for i in nums:
            if i in hashMap:
                hashMap[i] = hashMap[i] + 1
            else:
                hashMap[i] = 1
        res = []
        # print(hashMap)
        while k != 0 :
            maxValue = 0

            for key,value in hashMap.items():
                if maxValue < value:
                    maxValue = value
                    maxkey = key
            # print(maxkey,maxValue)
            hashMap.pop(maxkey)
            res.append(maxkey)
            # print(res)
            k -= 1

        return res
        
            

obj = Solution()

nums = [1,1,1,2,2,3]
k = 2
res = obj.topKFrequent(nums,k)
print(res)