class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        half_len = n // 2
        
        counts = [0] * 26
        for ch in s:
            counts[ord(ch) - ord('a')] += 1
            
        odd_char = ""
        odd_count = 0
        for i in range(26):
            if counts[i] % 2 != 0:
                odd_count += 1
                odd_char = chr(ord('a') + i)
                
        if (n % 2 == 0 and odd_count > 0) or (n % 2 == 1 and odd_count != 1):
            return ""

        half_counts = [counts[i] // 2 for i in range(26)]

        def build_min_palindrome(prefix_half, remaining_half, mid_ch=""):
            res = list(prefix_half)
            for c_idx in range(26):
                if remaining_half[c_idx] > 0:
                    res.extend([chr(ord('a') + c_idx)] * remaining_half[c_idx])
            first_half = "".join(res)
            return first_half + mid_ch + first_half[::-1]

        best_cand = None

        min_all = build_min_palindrome("", half_counts, odd_char if n % 2 == 1 else "")
        if min_all > target:
            best_cand = min_all

        for L in range(half_len + 1):
            curr_counts = list(half_counts)
            possible = True
            for i in range(L):
                c_idx = ord(target[i]) - ord('a')
                if curr_counts[c_idx] <= 0:
                    possible = False
                    break
                curr_counts[c_idx] -= 1
            
            if not possible:
                continue
                
            pref_str = target[:L]

            if L < half_len:
                t_char_idx = ord(target[L]) - ord('a')
                for c_idx in range(t_char_idx + 1, 26):
                    if curr_counts[c_idx] > 0:
                        next_counts = list(curr_counts)
                        next_counts[c_idx] -= 1
                        cand = build_min_palindrome(pref_str + chr(ord('a') + c_idx), next_counts, odd_char if n % 2 == 1 else "")
                        if cand > target and (best_cand is None or cand < best_cand):
                            best_cand = cand
            else:
                if n % 2 == 0:
                    cand = build_min_palindrome(pref_str, curr_counts)
                    if cand > target and (best_cand is None or cand < best_cand):
                        best_cand = cand
                else:
                    t_mid = target[half_len]
                    if ord(odd_char) >= ord(t_mid):
                        cand = build_min_palindrome(pref_str, curr_counts, odd_char)
                        if cand > target and (best_cand is None or cand < best_cand):
                            best_cand = cand

        return best_cand if best_cand is not None else ""