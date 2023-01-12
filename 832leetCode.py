# 832LeetCode

"""
class Solution(object):
    def flipAndInvertImage(self, image):
        

        for i in range(len(image)):
            
            image[i] = image[i][::-1]
            for digit in range(len(image[i])):
                if image[i][digit] == 0:
                    image[i][digit] = 1
                else: image[i][digit] = 0

        return image

"""


class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype
        """

        for singleImage in image:

            singleImage.reverse()   
            
            for i in range(len(singleImage)):
                if singleImage[i] == 0:
                    singleImage[i] = 1
                else:
                    singleImage[i] = 0

        return image



obj = Solution()

image = [[1,1,0],[1,0,1],[0,0,0]]

ans = obj.flipAndInvertImage(image)

print(ans)
