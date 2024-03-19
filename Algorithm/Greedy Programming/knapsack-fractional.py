class greedy:

    # return max_profit 
    def knapsack_fractional(self, weight,profit,max_weight):
        n = len(weight)
        pi_wi = [0] * n
        maxprofit = 0
        bagWeight = 0

        i = 0
        while i < n:
            pi_wi[i] = profit[i] / weight[i]
            i += 1
        
        while bagWeight <= max_weight and weight:
            print(pi_wi,bagWeight,maxprofit)
            maxW = max(pi_wi)
            index = pi_wi.index(maxW)
            if bagWeight + weight[index] > max_weight:
                diff_Weight = max_weight - bagWeight
                bagWeight += weight[index]
                maxprofit += pi_wi[index] * diff_Weight
                
            else:
                bagWeight += weight[index]
                maxprofit += profit[index]
            
            pi_wi.pop(index)
            weight.pop(index)
            profit.pop(index)


        return maxprofit

        
        




weight = [2,3,5,7,1,4,1]
profit = [10,5,15,7,6,18,3]
max_weight = 15

prob1 = greedy()
res = prob1.knapsack_fractional(weight,profit,max_weight)
print(res)