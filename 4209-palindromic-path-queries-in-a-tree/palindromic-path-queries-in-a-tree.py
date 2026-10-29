class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # LCA with Binary Lifting + Euler Tour setup
        LOG = 16
        up = [[0] * LOG for _ in range(n)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0
        
        # Array to store node masks
        masks = [1 << (ord(c) - ord('a')) for c in s]
        
        # Root-to-node XOR path initial values
        root_xor = [0] * n

        # DFS to initialize LCA tables, depth, and Euler tour times
        stack = [(0, 0, 0, 0)]  # (node, parent, state, current_xor)
        # We perform iterative DFS to prevent recursion depth issues in Python
        
        # Iterative DFS for pre-calculations
        parent = [0] * n
        order = []
        
        def dfs():
            nonlocal timer
            st = [(0, -1)]
            while st:
                u, p = st.pop()
                if u >= 0:
                    tin[u] = timer
                    timer += 1
                    order.append(u)
                    up[u][0] = p if p != -1 else u
                    for i in range(1, LOG):
                        up[u][i] = up[up[u][i - 1]][i - 1]
                    
                    st.append((~u, p))  # Marker for post-visit
                    for v in adj[u]:
                        if v != p:
                            depth[v] = depth[u] + 1
                            root_xor[v] = root_xor[u] ^ masks[v]
                            st.append((v, u))
                else:
                    u = ~u
                    tout[u] = timer - 1

        root_xor[0] = masks[0]
        dfs()

        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            for i in range(LOG - 1, -1, -1):
                if depth[u] - (1 << i) >= depth[v]:
                    u = up[u][i]
            if u == v:
                return u
            for i in range(LOG - 1, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
            return up[u][0]

        # Range XOR Fenwick Tree (Binary Indexed Tree)
        # Difference array BIT to support range XOR updates and point XOR queries
        bit = [0] * (timer + 2)

        def bit_update(idx, val):
            idx += 1
            while idx < len(bit):
                bit[idx] ^= val
                idx += idx & (-idx)

        def bit_query(idx):
            res = 0
            idx += 1
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res

        # Initialize BIT with initial root_xor values
        for i in range(n):
            # Apply range XOR update at tin[i]
            # Since root_xor[i] affects node i and its subtree
            pass

        # Construct initial BIT using Euler tour interval point updates
        for u in range(n):
            bit_update(tin[u], root_xor[u])
            bit_update(tin[u] + 1, root_xor[u])

        def get_current_root_xor(u):
            return bit_query(tin[u])

        # Re-build BIT for range update / point query pattern
        bit = [0] * (timer + 2)
        
        # Initializing BIT using difference technique:
        # A range XOR update [l, r] with val is achieved by:
        # update(l, val) and update(r + 1, val)
        for u in range(n):
            val = root_xor[u]
            bit_update(tin[u], val)
            bit_update(tin[u] + 1, val)
            
        # Re-initialize properly with Range Update Point Query
        bit = [0] * (timer + 2)
        
        # Direct point values for Euler tour:
        # To apply range update [tin[u], tout[u]] ^ val:
        # bit_update(tin[u], val) and bit_update(tout[u] + 1, val)
        for u in range(n):
            # Contribution of masks[u] to u's subtree [tin[u], tout[u]]
            bit_update(tin[u], masks[u])
            bit_update(tout[u] + 1, masks[u])

        ans = []

        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                new_mask = 1 << (ord(c) - ord('a'))
                diff = masks[u] ^ new_mask
                if diff != 0:
                    masks[u] = new_mask
                    # Update subtree range in Euler tour
                    bit_update(tin[u], diff)
                    bit_update(tout[u] + 1, diff)
            else:
                u = int(parts[1])
                v = int(parts[2])
                lca = get_lca(u, v)
                
                rx_u = bit_query(tin[u])
                rx_v = bit_query(tin[v])
                
                # Path XOR = RootXOR(u) ^ RootXOR(v) ^ node_mask(LCA)
                path_mask = rx_u ^ rx_v ^ masks[lca]
                
                # Check if at most 1 bit is set
                can_form_palindrome = (path_mask & (path_mask - 1)) == 0
                ans.append(can_form_palindrome)

        return ans