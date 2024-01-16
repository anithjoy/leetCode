class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """

        finalResult = []
        end = len(graph)-1
        print(end)

        def dfs(v,res=[]):
            res.append(v)

            if v == end :
                finalResult.append(res[:])
                return
            
            for eachNode in graph[v]:
                dfs(eachNode, res[:])

        dfs(0,[])
        return(finalResult)


        
                

graph = [[1,2], [3], [3], []]
obj = Solution()

print(obj.allPathsSourceTarget(graph))