class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # def counter(n):
        #     counter = 0
        #     for i in str(n):
        #         if int(i) == 1:
        #             counter += 1    

        #     return counter

        # ans = []
        # for i in range(n+1):
        #     bi = bin(i)
            
        #     ans.append(counter(int(bi.split("b")[1])))

            
        # return ans
    
    # ///////////////////////////////////////////////////////////////// neetCOde O(n log n) soln

        dp = [0]*(n +1 )
        offset = 1

        for i in range(1,n+1):
            if offset *2 == i:
                offset = i 
            dp[i] = 1 + dp[i - offset] 

        return dp


      




obj = Solution()

n = 5
ans = obj.countBits(n)

print(ans)