class Solution(object):
    list = []
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum = 0
        for i in str(n):
            sum = sum +int(i)**2
        if sum in self.list:
            return False
        
        self.list.append(sum)
        # print(self.list)
        if sum == 1:
            return True
        return self.isHappy(sum) 

obj = Solution()
n = 1

ans = obj.isHappy(n)
print(ans)