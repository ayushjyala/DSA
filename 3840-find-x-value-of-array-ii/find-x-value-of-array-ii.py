class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        tree_prod = [1] * (4 * n)
        tree_rem = [[0] * k for _ in range(4 * n)]
        
        def merge(u: int, left_child: int, right_child: int):
            tree_prod[u] = (tree_prod[left_child] * tree_prod[right_child]) % k
            p_left = tree_prod[left_child]
            
            for r in range(k):
                tree_rem[u][r] = tree_rem[left_child][r]
                
            for r in range(k):
                cnt = tree_rem[right_child][r]
                if cnt > 0:
                    tree_rem[u][(r * p_left) % k] += cnt

        def build(u: int, l: int, r: int):
            if l == r:
                val = nums[l] % k
                tree_prod[u] = val
                tree_rem[u][val] = 1
                return
            mid = (l + r) // 2
            build(2 * u, l, mid)
            build(2 * u + 1, mid + 1, r)
            merge(u, 2 * u, 2 * u + 1)

        def update(u: int, l: int, r: int, idx: int, val: int):
            if l == r:
                val %= k
                tree_prod[u] = val
                tree_rem[u] = [0] * k
                tree_rem[u][val] = 1
                return
            mid = (l + r) // 2
            if idx <= mid:
                update(2 * u, l, mid, idx, val)
            else:
                update(2 * u + 1, mid + 1, r, idx, val)
            merge(u, 2 * u, 2 * u + 1)

        def query(u: int, l: int, r: int, ql: int, qr: int):
            if ql <= l and r <= qr:
                return tree_prod[u], tree_rem[u]
            
            mid = (l + r) // 2
            if qr <= mid:
                return query(2 * u, l, mid, ql, qr)
            if ql > mid:
                return query(2 * u + 1, mid + 1, r, ql, qr)
            
            lp_prod, lp_rem = query(2 * u, l, mid, ql, qr)
            rp_prod, rp_rem = query(2 * u + 1, mid + 1, r, ql, qr)
            
            res_prod = (lp_prod * rp_prod) % k
            res_rem = list(lp_rem)
            
            for r_val in range(k):
                cnt = rp_rem[r_val]
                if cnt > 0:
                    res_rem[(r_val * lp_prod) % k] += cnt
                    
            return res_prod, res_rem

        build(1, 0, n - 1)
        ans = []

        for idx, val, start, x in queries:
            update(1, 0, n - 1, idx, val)
            _, rem_counts = query(1, 0, n - 1, start, n - 1)
            ans.append(rem_counts[x])

        return ans