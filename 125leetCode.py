# 125 leetCode


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = s.lower()
        
        
        # initializing pointers
        p1 = 0
        p2 = len(s) - 1

        while p1 < p2:
            if not s[p1].isalnum():
                p1 += 1
                continue

            if not s[p2].isalnum():
                p2 -= 1
                continue
            
            if s[p1] != s[p2]:
                return False
            else:
                p1 += 1
                p2 -= 1

        return True




        

obj1 = Solution()

# different inputs
s = "A man, a plan, a canal: Panama"
s = "race a car"
s = " "

ans = obj1.isPalindrome(s)


print(ans)
