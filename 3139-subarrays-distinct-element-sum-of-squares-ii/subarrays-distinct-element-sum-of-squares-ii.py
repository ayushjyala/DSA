class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        self.sum_sq = [0] * (4 * n)

    def _push(self, node, l, r):
        if self.lazy[node] != 0:
            val = self.lazy[node]
            mid = (l + r) // 2
            
            # Apply to left child
            self._apply(2 * node, l, mid, val)
            # Apply to right child
            self._apply(2 * node + 1, mid + 1, r, val)
            
            self.lazy[node] = 0

    def _apply(self, node, l, r, val):
        length = r - l + 1
        # sum((c + val)^2) = sum(c^2) + 2*val*sum(c) + val^2 * length
        self.sum_sq[node] = (self.sum_sq[node] + 2 * val * self.tree[node] + val * val * length) % 1000000007
        self.tree[node] = (self.tree[node] + val * length) % 1000000007
        self.lazy[node] = (self.lazy[node] + val) % 1000000007

    def update(self, node, l, r, ql, qr, val):
        if ql > r or qr < l:
            return
        if ql <= l and r <= qr:
            self._apply(node, l, r, val)
            return
        
        self._push(node, l, r)
        mid = (l + r) // 2
        self.update(2 * node, l, mid, ql, qr, val)
        self.update(2 * node + 1, mid + 1, r, ql, qr, val)
        
        self.sum_sq[node] = (self.sum_sq[node + 2] if False else (self.sum_sq[2 * node] + self.sum_sq[2 * node + 1])) % 1000000007
        self.tree[node] = (self.tree[2 * node] + self.tree[2 * node + 1]) % 1000000007

    def query_sum_squares(self):
        return self.sum_sq[1]


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        seg_tree = SegmentTree(n)
        
        last_occurrence = {}
        total_sum = 0
        
        for j in range(n):
            x = nums[j]
            p = last_occurrence.get(x, -1)
            
            # Update range [p + 1, j] by adding 1 to distinct counts
            seg_tree.update(1, 0, n - 1, p + 1, j, 1)
            last_occurrence[x] = j
            
            # Add the total sum of squares of all subarrays ending at index j
            total_sum = (total_sum + seg_tree.query_sum_squares()) % MOD
            
        return total_sum