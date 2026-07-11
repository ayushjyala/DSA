class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        arr = sorted((nums[i], i) for i in range(n))

        pos = [0] * n
        comp = [0] * n

        cid = 0
        for i, (_, idx) in enumerate(arr):
            pos[idx] = i
            if i and arr[i][0] - arr[i - 1][0] > maxDiff:
                cid += 1
            comp[i] = cid

        # farthest reachable in one edge
        nxt = list(range(n))
        j = 0
        for i in range(n):
            while j + 1 < n and arr[j + 1][0] - arr[i][0] <= maxDiff:
                j += 1
            nxt[i] = j

        LOG = (n).bit_length()

        up = [nxt]
        for _ in range(LOG - 1):
            prev = up[-1]
            cur = [0] * n
            for i in range(n):
                cur[i] = prev[prev[i]]
            up.append(cur)

        ans = []

        for u, v in queries:
            if u == v:
                ans.append(0)
                continue

            pu = pos[u]
            pv = pos[v]

            if comp[pu] != comp[pv]:
                ans.append(-1)
                continue

            if pu > pv:
                pu, pv = pv, pu

            cur = pu
            res = 0

            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < pv:
                    cur = up[k][cur]
                    res += 1 << k

            ans.append(res + 1)

        return ans