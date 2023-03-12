class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # totalCost = 0
        # if(len(cost)>3):
        #     i = 0
        #     while(i < (len(cost)-1)):
        #         if(cost[i] >= cost[i+1]):
        #             totalCost += cost[i+1]
        #             i = i+2
        #             print("if 1",i-1)
                    
        #         else:
        #             totalCost += cost[i]
        #             i = i+1
        #             print("if 2",i-1)

        #     return totalCost
        
        # elif(len(cost) == 2):
            
        #     if(cost[0]> cost[1]):
        #         return cost[1]
        #     else:
        #         return cost[0]
            
        # elif(len(cost) == 1):
        #     return cost[0]
        # else:
        #     if(cost[0]+cost[2] > cost[1]):
        #         return cost[1]
        #     else:
        #         return cost[0]+cost[2]

        # totalCost = 0
        # # if(len(cost)>3):
        # i = 0
        # while(i < (len(cost)-1)):
        #     print(i)
        #     if(i+2) < len(cost)-1:
        #         if(cost[i]>=cost[i+1]):
        #             print("1st ran",cost[i+1])
        #             totalCost += cost[i+1]
        #             i=i+2
        #         else:
        #             print("2nde ran",cost[i])
        #             totalCost += cost[i]
        #             i=i+1
        #     else:
        #         if(cost[i]+cost[i+2]<cost[i+1]):
        #             print("3rd ran",(cost[i]+cost[i+2]))
        #             totalCost += (cost[i]+cost[i+2])
        #             i += 3
        #         else:
        #             print("4th ran",cost[i+1])
        #             totalCost += cost[i+1]
        #             i += 2


        # return totalCost

        # dynamic programming porblem from neetCode  https://www.youtube.com/watch?v=ktmzAZWkEZ0&ab_channel=NeetCode

        cost.append(0)

        for i in range(len(cost)-3, -1, -1):
            cost[i] = cost[i] + min( cost[i+1], cost[i+2])

        return min(cost[0], cost[1])






        


obj = Solution()
# cost = [10,15,20]
cost = [1,100,1,1,1,100,1,1,100,1]
# cost =[0,0,0,0]
res = obj.minCostClimbingStairs(cost)

print(res)