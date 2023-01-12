# 917 leetcode

class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        j = len(s) - 1
        output = ""

        while(i < len(s) and j != -1):
            if not s[i].isalpha():
                output += s[i]
                i += 1
                continue
        
            elif not s[j].isalpha():
                j -= 1
                continue

            elif s[i].isalpha() and s[j].isalpha():
                output += s[j]
                j -= 1
                i += 1
                continue

        while(i < len(s)):
            print("running")
            output += s[i]
            i += 1

        

        return output

obj = Solution()

s = "ab-cd"
s = "a-bC-dEf-ghIj"
s = "!Test1ng-Leet=code-Q!"

ans = obj.reverseOnlyLetters(s)

print(ans)
            
                


