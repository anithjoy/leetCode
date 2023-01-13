class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        
        sell = None
        profit = 0
        
        statusBuy = False
        print(prices)

         

        for i in range(len(prices)):

            if (not statusBuy) and i+1 < len(prices) and prices[i] > prices[i+1] :
                continue
            elif not statusBuy:
                buy = prices[i]
                print("buy:" , buy,i)
                statusBuy = True

            if statusBuy and i+1 < len(prices) and prices[i] < prices[i+1] : 
                continue
            elif statusBuy: 
                sell = prices[i]
                print("sell:" , sell,1)

            profit = profit + (sell-buy)
            statusBuy = False
        return profit 


        # # neetCode solution
        # profit = 0

        # for i in range(1,len(prices)):
        #     if prices[i] > prices[i-1]:
        #         profit += (prices[i] - prices[i-1])

        # return profit

            
        
        

obj1 = Solution()

prices = [7,1,5,3,6,4]
prices = [1,2,3,4,5]
prices = [7,6,4,3,1]
prices = [7,1,2,3,1,4,5,6,2,9]

ans = obj1.maxProfit(prices)

print(ans)
