class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 0
        buy = None
        sell = None
        profit = 0

        while( i < len(prices)):
            
            if buy is None:
                buy = prices[i]
                # print("buy is *",buy)
                i += 1
                continue

            if i+1 < len(prices) and buy > prices[i] :
                buy = prices[i]
                # print("buy is",buy)
                i += 1
                continue

            sell = prices[i]
            # print("sell is",sell)

            profit = max(profit, sell-buy)
            # print("profit is",profit)
            i += 1



        return profit


obj1 = Solution()

prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
prices = [1]

ans = obj1.maxProfit(prices)

print(ans)