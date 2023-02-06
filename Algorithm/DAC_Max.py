# Find maximum  number from array using Divide and conquer technqiue

my_arr = [1, 40, 3, 4, 30, 25, 7, 8, 9, 10]

def findMax(my_arr):

    # condition also known as base contion

    if len(my_arr) == 1:
        return my_arr[0]

    # Divide the array into 2 arrays and call it recursively\

    mid = len(my_arr)//2
    left = findMax(my_arr[:mid])    #here this will return single element
    right = findMax(my_arr[mid : ])     #here this will return single element 
    maximum = max(left, right)

    return maximum
ans = findMax(my_arr)

print(ans)