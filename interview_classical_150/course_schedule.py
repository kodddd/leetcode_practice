import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        valid = True
        visited = [0] * numCourses
        edges = collections.defaultdict(list)
        for info in prerequisites:
            edges[info[1]].append(info[0])

        def dfs(u: int):
            nonlocal valid
            visited[u] = 1
            for to in edges[u]:
                if visited[to] == 0:
                    dfs(to)
                    if not valid:
                        return
                elif visited[to] == 1:
                    valid = False
                    return
            visited[u] = 2

        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)
        return valid
