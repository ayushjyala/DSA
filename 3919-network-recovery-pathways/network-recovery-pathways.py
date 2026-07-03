class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        """
        :type edges: List[List[int]]
        :type online: List[bool]
        :type k: int
        :rtype: int
        """
        n = len(online)

        adj = [[] for _ in range(n)]
        indeg = [0] * n
        costs = []

        for u, v, c in edges:
            adj[u].append((v, c))
            indeg[v] += 1
            costs.append(c)

        q = []
        for i in range(n):
            if indeg[i] == 0:
                q.append(i)

        topo = []
        head = 0

        while head < len(q):
            u = q[head]
            head += 1
            topo.append(u)

            for v, _ in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        costs = sorted(set(costs))

        def can(limit):
            INF = 10**18
            dist = [INF] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == INF:
                    continue

                if u != 0 and u != n - 1 and not online[u]:
                    continue

                for v, c in adj[u]:
                    if c < limit:
                        continue

                    if v != n - 1 and not online[v]:
                        continue

                    if dist[u] + c < dist[v]:
                        dist[v] = dist[u] + c

            return dist[n - 1] <= k

        left, right = 0, len(costs) - 1
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if can(costs[mid]):
                ans = costs[mid]
                left = mid + 1
            else:
                right = mid - 1

        return ans