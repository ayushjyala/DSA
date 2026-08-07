import math

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        temp = t
        for i in range(2, 10):
            while temp % i == 0:
                temp /= i
        if temp > 1: 
            return "-1"

        n = len(num)
        rem = [0] * (n + 1)
        rem[0] = t
        pos = n - 1
        num_list = list(num)
        for i in range(n):
            if num_list[i] == '0':
                pos = i
                break
            rem[i + 1] = rem[i] // math.gcd(rem[i], int(num_list[i]))

        if rem[n] == 1 and '0' not in num: 
            return num

        for i in range(pos, -1, -1):
            start = int(num_list[i]) + 1 if i < len(num_list) else 1
            for d in range(start, 10):
                t0 = rem[i] // math.gcd(rem[i], d)
                suffix = []
                curr_t = t0
                for j in range(n - 1, i, -1):
                    for v in range(9, 0, -1):
                        if curr_t % v == 0:
                            suffix.append(str(v))
                            curr_t /= v
                            break
                if curr_t == 1:
                    return "".join(num_list[:i]) + str(d) + "".join(suffix[::-1])

        curr_t = t
        digits = []
        for v in range(9, 1, -1):
            while curr_t % v == 0:
                digits.append(str(v))
                curr_t /= v
        req_len = max(n + 1, len(digits))
        return "1" * (req_len - len(digits)) + "".join(sorted(digits))