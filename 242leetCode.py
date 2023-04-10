# # 242leetCode
"""Below is the code for comparing two dictionaries in Python"""
# dict1 = {'Name': 'asif', 'Age': 5}
# dict2 = {'Name': 'asif', 'Age': 5}
 
# if dict1 == dict2:
#     print ("dict1 is equal to dict2")
# else:
#     print ("dict1 is not equal to dict2")


# class Solution(object):
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         # creating a hashMap
#         hashMap1 = {}
#         hashMap2 = {}

        
#         if not (len(s)) == (len(t)):
#             return False

#         for digit in range(len(s)):
#             hashMap1[s[digit]] = hashMap1.get(s[digit], 0) + 1
#             hashMap2[t[digit]] = hashMap2.get(t[digit], 0) + 1

#         if hashMap1 == hashMap2:
#             return True

#         return False


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        hashMapS = {}


        for letter in s:
            if letter in hashMapS:
                hashMapS[letter] += 1
            else:
                hashMapS[letter] = 1

        for letter in t:
            if letter in hashMapS:
                if hashMapS[letter] == 1:
                    hashMapS.pop(letter)
                else:
                    hashMapS[letter] -= 1
            else:
                return False

        if(len(hashMapS) == 0):
            return True
        return False
            
        

        

obj1 = Solution()
s = "gai"
t = "aig"

ans = obj1.isAnagram(s, t)

print(ans)


