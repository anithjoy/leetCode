
def insertionSort(num):

    for i in range(1,len(num)):
        key = num[i]
        j = i-1

        while j >= 0 and key < num[j]:
            num[j+1] = num[j]
            j -= 1 

        num[j+1] = key

    return num 




num = [5,8,3,9,1,7,2,6,4]
res = insertionSort(num)
print(res)