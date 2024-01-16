class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        def bfs(path):

            if graph[path[-1]] == path[-1]-1:
                res.append(path)
                return

            for node in graph[path[-1]]:
                bfs(path.append(node))

        bfs([0])
        return res
                

graph = [[1,2], [3], [3], []]
obj = Solution()

print(obj.allPathsSourceTarget(graph))