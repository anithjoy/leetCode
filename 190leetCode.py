# incomplete program

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = str(n)[::-1]
        n = "0b"+ n
        return int(n,2)
        




obj = Solution()

n =10100101000001111010011100

res = obj.reverseBits(n)
print(res)
