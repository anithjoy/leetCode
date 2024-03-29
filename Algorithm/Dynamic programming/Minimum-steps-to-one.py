"""Problem Statement:
On a positive integer, you can perform any one of the following 3 steps. 1.) Subtract 1 from it. ( n = n - 1 ) , 2.) If its divisible by 2, divide by 2. ( if n % 2 == 0 , then n = n / 2 ) , 3.) If its divisible by 3, divide by 3. ( if n % 3 == 0 , then n = n / 3 ). Now the question is, given a positive integer n, find the minimum number of steps that takes n to 1

eg: 1.)For n = 1 , output: 0 2.) For n = 4 , output: 2 ( 4 /2 = 2 /2 = 1 ) 3.) For n = 7 , output: 3 ( 7 -1 = 6 /3 = 2 /2 = 1 )"""


class DP:
    def __init__(self):
        self.memo = {} # key-n , value-number of steps

    def solve(self,n):

        # base Case
        if n<= 1:
            return 0
        
        if n not in self.memo:
            # value1
            value1 = 1 + self.solve(n-1)

            # value2
            value2 = 1 + self.solve(n//2) if n % 2 == 0 else float('inf')

            # value3
            value3 = 1 + self.solve(n//3) if n % 3 == 0 else float('inf')

            # find minimum of all the values and save it to memo
            self.memo[n] = min(value1,value2,value3)


        return self.memo[n]
        

prob1 = DP()
for n in range(11):
    res = prob1.solve(n)
    print(f'{n} = {res}')
