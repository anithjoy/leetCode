
def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        mid = len(arr) // 2
        left_max = find_max(arr[:mid])
        right_max = find_max(arr[mid:])
        return max(left_max, right_max)

my_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(find_max(my_arr)) # Output: 10

