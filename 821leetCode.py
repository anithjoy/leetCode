#  821 leet Code

class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        occurences = []
        result = []
        value = None
        for i in range(len(s)):
            if s[i] == c:
                occurences.append(i)

        for i in range(len(s)):
            for j in occurences:
                if  value is  None:
                    value = len(s)
                    
                value = abs(min(value,j - i))
            result.append(value)

        return result     

obj = Solution()

s = "loveleetcode"
c = "e"

ans = obj.shortestToChar(s,c)

print(ans)
