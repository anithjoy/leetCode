"""Given an array of unsorted elements, the idea is to find the length of the longest subsequence whose elements are in ascending order (from lowest to highest).

The elements in the subsequence do not necessarily have to appear in consecutive positions in the initial array, and the solution of LIS is not always unique.

2.1. Example
For elements {-3, 10, 5, 12, 15} we identify the following increasing subsequences.

-3, 10, 12, 15
-3, 5, 12, 15
10, 12, 15
5, 12, 15
12, 15
As we can see from the list, the longest increasing subsequence is {-3, 5, 12, 15} with length 4. However, it’s not the only solution, as {-3, 10, 12, 15} is also the longest increasing subsequence with equal length.

"""


class DP:
    def __init__(self,input) -> None:
        self.dp = [1] * len(input)

        self.lis(input)
        

    def lis(self,input):

        for i in range(1, len(input)):

            for j in range(i):

                if input[i] > input[j] and self.dp[i] < self.dp[j]+1:
                    self.dp[i] = self.dp[j] + 1

        print(self.dp)
        return (max(self.dp))
    

input = [-3,10,5,12,15]
prob = DP(input)
print(prob)