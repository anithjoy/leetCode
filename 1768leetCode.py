
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i,j  = 0,0
        # pointer for word1 and word2 respectively

        output = ""
        while( i < len(word1) and j < len(word2)):
            output += word1[i]
            i += 1
            output += word2[j]
            j += 1
        while(i <len(word1)):
            output += word1[i]
            i += 1

        while(j <len(word2)):
            output += word2[j]
            j += 1

        return output

    
obj1 = Solution()

word1 = "abc"
word2 = "pqr"

ans = obj1.mergeAlternately(word1, word2)

print(ans)

