class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
# check this later
        # delete = 1
        # p1 = 0
        # p2 = len(s)-1

        # while p1 <= p2:
        #     if s[p1] == s[p2]:
        #         p1 += 1
        #         p2 -= 1
        #         continue
        #     elif s[p1] != s[p2] and delete != 0:
        #         if s[p1+1]== s[p2]:
        #             p1 +=1
        #         else:
        #             p2 -= 1
        #         delete -= 1
        #         continue
        #     else:
        #         return False

        # return True

        l,r = 0, len(s)-1
        while l < r :
            if s[l] != s[r]:
                skipL, skipR = s[l+1:r+1], s[l: r]
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            l,r = l+1,r-1
        return True
    

obj = Solution()

s = "aba"
s = "abca"
s = "abc"
s ="aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"

res = obj.validPalindrome(s)
print(res)
