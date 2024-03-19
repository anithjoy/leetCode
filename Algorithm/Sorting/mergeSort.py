
def mergeSort(nums):
    if len(nums) > 1:
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        print(left, right) 
        mergeSort(left)
        mergeSort(right)
        print(left, right) # For a better understanding of the recursion

        l,r,k = 0,0,0
        
        while l< len(left) and r < len(right):
            if left[l] >= right[r]:
                nums[k] = right[r]
                r += 1
                
            else:
                nums[k] = left[l]
                l+= 1
            k += 1

        while l < len(left):
            nums[k] = left[l]
            l += 1
            k += 1

        while r < len(right):
            nums[k] = right[r]
            r += 1
            k += 1


    return nums


num = [5,8,3,9,1,7,2,6,4]
res = mergeSort(num)
print(res)

        
            


        


