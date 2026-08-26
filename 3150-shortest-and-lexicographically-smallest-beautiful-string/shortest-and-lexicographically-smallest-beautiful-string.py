class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = []

        for i, ch in enumerate(s):
            if ch == '1':
                ones.append(i)

        if len(ones) < k:
            return ""

        ans = ""

        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]

            curr = s[start:end + 1]

            if not ans or len(curr) < len(ans) or (len(curr) == len(ans) and curr < ans):
                ans = curr

        return ans