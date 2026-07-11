class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        def dfs(node):
            visited[node] = True
            nodes = 1
            edge_count = len(graph[node])

            for nei in graph[node]:
                if not visited[nei]:
                    n_nodes, n_edges = dfs(nei)
                    nodes += n_nodes
                    edge_count += n_edges

            return nodes, edge_count

        for i in range(n):
            if not visited[i]:
                nodes, edge_count = dfs(i)
                actual_edges = edge_count // 2
                required_edges = nodes * (nodes - 1) // 2

                if actual_edges == required_edges:
                    ans += 1

        return ans