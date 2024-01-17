class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        edges.sort()
        destination = set()

        for de in edges:
            destination.add(de[1])

        result = [i for i in range(n) if i not in destination]
        return result

graph = [[0,1],[0,2],[2,5],[3,4],[4,2]]
e=6
obj = Solution()

print(obj.findSmallestSetOfVertices(e,graph))