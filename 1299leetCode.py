class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        res= []
        index = 0
        # maxEle = 0
        # # prevIndex = 0
        # for i in range(len(arr)-1):     #0, 1
        #     # print(i,index,maxEle)
        #     if(i == index ):            #0 , 1
        #         maxEle = max(arr[index+1:])     #18 , 6
        #         index = arr.index(maxEle)       #1, 4
        #     res.append(maxEle)
                

        # res.append(-1)
        # return res

        rightMax = -1

        for i in range(len(arr)-1,-1,-1):
            currMax = max(rightMax,arr[i])
            arr[i] = rightMax
            rightMax = currMax

        return arr
    
obj = Solution()

arr = [17,18,5,4,18,1]
# arr = [0,0,0,0,0,0]
# arr = [400]

res = obj.replaceElements(arr)

print(res)