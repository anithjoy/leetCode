class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # counter = 0
        # for i in str(n):
        #     if int(i) == 1:
        #         counter += 1

        # return counter

        # ////////////////////////////////////////////////////////////
        res = 0

        while n:
            res += n % 2
            n = n >> 1
        return res

obj = Solution()

n =00000000000000000000000000001011

res = obj.hammingWeight(n)
print(res)