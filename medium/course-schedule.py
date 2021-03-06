class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]

        for x,y in prerequisites:
            graph[x].append(y)

        def dfs(idx):
            if visited[idx] == -1:
                return False
            if visited[idx] == 1:
                return True

            visited[idx] = -1
            for j in graph[idx]:
                if not dfs(j):
                    return False

            visited[idx] = 1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
