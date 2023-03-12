import math
class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """

        maxIt = math.ceil(len(weights)/days)
        weights.sort()
        i = 0
        maxWeight = max(weights)

        while i < days:
            sum = sum + weights[i]
            maxWeight = max(maxWeight,sum)
            i += 1

        for i in range (len(weights)):
            if (i< days & i<maxIt):





