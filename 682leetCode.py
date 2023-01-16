class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """

        stack = []
        

        for op in operations:

            if op == "+":
                stack.append(stack[-1] + stack[-2])

            elif op == "D":
                stack.append(stack[-1] * 2)

            elif op == "C":
                stack.pop()

            else:
                stack.append(int(op))

        return sum(stack)

        # for s in stack:
        #     sum += s

        # return sum

            
obj = Solution()

ops = ["5","2","C","D","+"]
ops = ["5","-2","4","C","D","9","+","+"]

ans = obj.calPoints(ops)

print(ans)