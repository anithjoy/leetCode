
def partition(nums,start,end):
    
    pivot = nums[end]
    i = start

    for j in range(start,end):
        if nums[j] <= pivot:
            nums[i],nums[j] = nums[j],nums[i]
            i += 1

    nums[i],nums[end] = nums[end], nums[i]
    return i


def quickSort(nums,start,end):

    if start >= end: return
        
    
    pi = partition(nums,start,end)

    quickSort(nums,start,pi-1)
    quickSort(nums, pi+1, end)

    return nums


nums = [5,8,3,9,1,7,2,6,4]
res = quickSort(nums,0,len(nums)-1)
print(res)