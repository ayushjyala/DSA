class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        leftSum = rightSum = 0
        leftQ = rightQ = 0

        for i in range(n // 2):
            if num[i] == '?':
                leftQ += 1
            else:
                leftSum += int(num[i])

        for i in range(n // 2, n):
            if num[i] == '?':
                rightQ += 1
            else:
                rightSum += int(num[i])

        if (leftQ + rightQ) % 2:
            return True

        return (leftSum - rightSum) != (rightQ - leftQ) // 2 * 9