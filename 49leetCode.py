class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # res= {}

        # for s in strs:
        #     sorted_s = "".join(sorted(s))
        #     if sorted_s in res:
        #         res[sorted_s].append(s)
        #     else:
        #         res[sorted_s] = [s]

        # return res.values()

        hashmap = {}

        for i in strs:
            string ="".join(sorted(i)) # will give us array
            if string in hashmap:
                hashmap[string].append(i)
            else:
                hashmap[string]=[i]

        return hashmap.values()


obj = Solution()

strs = ["eat","tea","tan","ate","nat","bat"]
res = obj.groupAnagrams(strs)

print(res)