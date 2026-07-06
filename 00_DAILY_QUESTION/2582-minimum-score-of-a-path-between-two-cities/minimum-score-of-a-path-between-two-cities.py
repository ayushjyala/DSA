class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        graph = [[] for _ in range(n + 1)]

        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        stack = [1]
        visited = [False] * (n + 1)
        visited[1] = True

        ans = float('inf')

        while stack:
            node = stack.pop()

            for nei, w in graph[node]:
                ans = min(ans, w)

                if not visited[nei]:
                    visited[nei] = True
                    stack.append(nei)

        return ans