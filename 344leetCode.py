class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s)-1
        for i in range(len(s)//2):
            storage = s[l]
            s[l] = s[r]
            s[r] = storage
            l += 1
            r -= 1

        return s
