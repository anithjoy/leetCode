
# priority queue => orders element by priority
# it is tree data structure
# 2 type of heap - min heap and max heap
# MIn heap - smallest is th ehighest priority, max heap - largest is the priority
# heapify - to bring tree in proper tree order is called heapify
# for using heap property we have to import heapq
# offer min heap


# if you are at the node I => left child position => 2*i+1, right child position=> 2*i+2


import heapq as hq

data = [10,20,43,1,2,65,17,44,2,3,1]  
print(data)
hq.heapify(data)

print("heapified ",data)

print("heap Pop ",hq.heappop(data))

print("when we print the data, it will return the data after heapified. It is heapified already",data)

# whenever you use heappsuh. This library will do heapify everytime fro you.
hq.heappush(data,2)

print(data)


# the above procedure is for min heap
#  for max heap. negate the data 
# data = [-x for x in data]

# or u can use inbuild max heapify function

hq._heapify_max(data)
print("Max heap data",data)

print(hq.heappop(data))

print(data) 