# BInary Search
# it is a DAC technique




def bs(my_arr,target):
    left = 0
    right = len(my_arr) - 1
    while left <= right:
        mid = (left + right) // 2

        # Base Condition 
        if my_arr[mid] == target:
            return True

        elif my_arr[mid] > target:
            right = mid - 1

        else: left = mid + 1

    return False

my_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

target = 0

ans = bs(my_arr,target)

print(ans)

    

     