class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        # I am going to use dfs approach on this problem by using stack and going to remove rooms when visited from visited
        visited = set(range(1,len(rooms)))
        stack = [num for num in rooms[0]]

        while stack:
            roomNum = stack.pop()
            if roomNum in visited:
                visited.remove(roomNum)

            for num in rooms[roomNum]:
                if num in visited:
                    stack.append(num)

        return len(visited)==0