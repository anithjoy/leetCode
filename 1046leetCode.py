class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while(len(stones) > 2):
            stones.sort(reverse = True)
            diff = abs (stones[0] - stones[1])
            stones.pop(0)
            stones.pop(0)
            
            if diff != 0:
                stones.append(diff)

        if len(stones) == 2 and abs(stones[0] - stones[1]) == 0 :
            return 0
        elif len(stones) == 1:
            return stones[0]
        else:
            return abs(stones[0] - stones[1])

                
            


obj = Solution()

# Input
stones = [2,7,4,1,8,1]
stones = [1,1,2]
stones = [3,7,2]


ans = obj.lastStoneWeight(stones)
print(ans)