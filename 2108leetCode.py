# 2108 LeetCode

class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        

        for word in words:
            if word ==word[::-1]:
                return word

        return ""

obj = Solution()

words = ["abc","car","ada","racecar","cool"]

ans = obj.firstPalindrome(words)

print(ans)
