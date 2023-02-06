# fibonacci number is DP problem
# find the nth term of the fibo series
# the below code takes O(2^n) time

# def fibo(n):

#     if n <= 1:
#         return n

#     return fibo(n-2)+fibo(n-1)


# we have to decrease the time so

def fibo(n):
    memory = [-1]*(n+1)
    
    if n <= 1:
        return n

    memory[0] = 0
    memory[1] = 1

    for i in range(2,n+1):
        memory[i] = memory[i-1] + memory[i-2]

    return memory

n=6

ans = fibo(n)

print(ans)