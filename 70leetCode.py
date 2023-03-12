class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        storage = [0,1,2]

        for i in range(3,n+1):
            value = storage[i-1]+storage[i-2]
            storage.append(value)
            # print(value) 

        
        return storage[n]
    

obj =  Solution()
n=5
ans = obj.climbStairs(n)
print(ans)