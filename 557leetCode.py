# 557 leetCode

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s:
            return s

        words = s.split()
        reverseWords = []

        for word in words:
            reverseWords.append(word[::-1])
            
        return " ".join(reverseWords)


obj1 = Solution()

s = "Let's take LeetCode contest"

ans = obj1.reverseWords(s)

print(ans)