class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ans = 0

        for row in range(-n + 1, n):
            for col in range(-n + 1, n):

                count = 0

                for i in range(n):
                    for j in range(n):

                        ni = i + row
                        nj = j + col

                        if 0 <= ni < n and 0 <= nj < n:
                            if img1[i][j] == 1 and img2[ni][nj] == 1:
                                count += 1

                ans = max(ans, count)

        return ans