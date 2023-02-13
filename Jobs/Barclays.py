# complete later

integers = [5,9,8,7,16]
maxNum = 3
storage = []

# convert each element into binary form

def convert(integer):
    if integer == 0:
        return 0
    next = integer//2
    next = convert(next)
    current = integer % 2
    string =  (str(current) + str(next))
    return string
    
array = []
for i in integers:
   array.append(convert(i))

arrayCounter = []
for i in array:
    counter = 0
    for j in i:
        if j=="1":
            counter += 1
    arrayCounter.append(counter)

print(arrayCounter)

i = 0
while i< maxNum:
    maxi = max(arrayCounter)
    for j in range(len(arrayCounter)):
        if arrayCounter[j] == maxi:
            storage.append(array[i])
            break
    i += 1

print(storage)







    