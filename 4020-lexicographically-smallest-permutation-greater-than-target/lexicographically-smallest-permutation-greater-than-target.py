class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        s_counts = {}
        for ch in s:
            s_counts[ch] = s_counts.get(ch, 0) + 1

        target_counts = {}
        best_L = -1
        best_next_char = None
        
        for i in range(n):
            can_cover = True
            for ch, count in target_counts.items():
                if s_counts.get(ch, 0) < count:
                    can_cover = False
                    break
            
            if not can_cover:
                break
            
            rem_counts = {ch: s_counts[ch] - target_counts.get(ch, 0) for ch in s_counts}
            t_char = target[i]
            
            for ch in sorted(rem_counts.keys()):
                if ch > t_char and rem_counts[ch] > 0:
                    best_L = i
                    best_next_char = ch
                    break
            
            target_counts[target[i]] = target_counts.get(target[i], 0) + 1

        if best_L == -1:
            return ""

        res = list(target[:best_L])
        
        prefix_counts = {}
        for ch in res:
            prefix_counts[ch] = prefix_counts.get(ch, 0) + 1
            
        rem_counts = {ch: s_counts[ch] - prefix_counts.get(ch, 0) for ch in s_counts}
        
        res.append(best_next_char)
        rem_counts[best_next_char] -= 1
        
        for ch in sorted(rem_counts.keys()):
            res.extend([ch] * rem_counts[ch])
            
        return "".join(res)