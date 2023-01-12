class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in range(len(s)-3 + 1):

            if s[i] == s[i+1] or s[i+1] == s[i+2] or s[i+2] == s[i]:
                continue
            else:
                result += 1

        return result

obj1 = Solution()

s = "xyzzaz"
s = "aababcabc"

ans = obj1.countGoodSubstrings(s) 

print(ans)
