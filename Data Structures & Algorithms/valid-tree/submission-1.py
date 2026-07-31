class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n <= len(edges):
            return False
        
        visited = set()
        adjList = {i: [] for i in range(n)}
        for start, end in edges:
            adjList[start].append(end)
            adjList[end].append(start)

        def dfs(node, par):
            if node in visited: # cycle detection
                return False

            visited.add(node)
            for neighbors in adjList[node]:
                if neighbors == par:
                    continue
                if not dfs(neighbors, node):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n

            
        