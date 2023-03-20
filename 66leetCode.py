class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # # below solution worked
        
        # characters = ""
        # for i  in digits:
        #     characters += str(i)
        
        # characters = str(int(characters) + 1)
        
        # resList = []
        # for i in characters:
        #     resList.append(int(i))
        # return resList
    
    # different manner of solution
    

obj = Solution()

digits = [1,2,3]


res = obj.plusOne(digits)

print(res)