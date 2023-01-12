# 2011leetCode

class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """

        res = 0

        if not operations:
            return res

        for i in operations:
            if (i == "X++" or i == "++X") :
                res += 1
            elif (i == "X--" or i == "--X") :
                res -= 1
            else :
                continue

        return res




operations = ["X++","++X","--X","X--"]
operations = ["++X","++X","X++"]

object1 = Solution()

ans = object1.finalValueAfterOperations(operations)

print(ans)

