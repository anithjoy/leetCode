class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # # splicing
        # nums1 = nums1[:m]
        # nums2 = nums2[:n]

        # print(nums1,nums2)

        # res = []
        
        # i,j = 0,0
        # while i < m and j < n:
        #     if (nums1[i] <= nums2[j]):
        #         res.append(nums1[i])
        #         i += 1
        #     else:
        #         res.append(nums2[j])
        #         j += 1

        # print("i,m,j,n",i,m,j,n)
        # if( i < m):
        #     res.extend(nums1[i:])
        # if( j< n):
        #     res.extend(nums2[j:])

        # return res

        lastIndex = m+n-1

        while m > 0 and n > 0:
            
            if (nums1[m-1] >= nums2[n-1]):
                nums1[lastIndex] = nums1[m-1]
                m -= 1
            else:
                nums1[lastIndex] = nums2[n-1]
                n -= 1

            lastIndex -= 1

        while n > 0:
            nums1[lastIndex] = nums2[n-1]
            lastIndex , n = lastIndex - 1 , n-1

        return nums1 


    
obj = Solution()

# test case 1
nums1 = [1,2,3,0,0,0] 
m = 3
nums2 = [2,5,6] 
n = 3

nums1 =[0]
m =0
nums2 =[1]
n =1


# testCase 2

res = obj.merge(nums1,m,nums2,n)
print(res)