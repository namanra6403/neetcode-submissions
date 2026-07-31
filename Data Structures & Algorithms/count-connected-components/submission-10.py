import sys
input = sys.stdin.readline
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        visited = set()

        adjList = [[] for _ in range(n)]
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in adjList[node]:
                dfs(neighbor)
            return True

        for node in range(n):
            if dfs(node):
                res += 1

        return res