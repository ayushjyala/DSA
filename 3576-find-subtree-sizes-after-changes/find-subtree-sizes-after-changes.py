from typing import List


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for node in range(1, n):
            adj[parent[node]].append(node)

        # Tracks closest ancestor for each character 'a'..'z' along current DFS path
        last_seen = [-1] * 26
        # Stores the final parent of each node after simultaneous re-parenting
        final_parent = parent[:]
        # Each node starts with subtree size 1 (itself)
        subtree_size = [1] * n

        def dfs_reparent(u: int) -> None:
            c = ord(s[u]) - ord("a")
            if last_seen[c] != -1:
                final_parent[u] = last_seen[c]

            prev = last_seen[c]
            last_seen[c] = u

            for v in adj[u]:
                dfs_reparent(v)

            last_seen[c] = prev

        def dfs_size(u: int) -> None:
            for v in adj[u]:
                dfs_size(v)
            if u != 0:
                subtree_size[final_parent[u]] += subtree_size[u]

        dfs_reparent(0)
        dfs_size(0)
        return subtree_size