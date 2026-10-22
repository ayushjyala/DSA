from collections import deque

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
            
        # Check if nums is cyclically increasing or cyclically decreasing
        inc_breaks = 0
        dec_breaks = 0
        for i in range(n):
            if (nums[i] + 1) % n != nums[(i + 1) % n]:
                inc_breaks += 1
            if (nums[i] - 1) % n != nums[(i + 1) % n]:
                dec_breaks += 1
                
        is_inc = inc_breaks <= 1
        is_dec = dec_breaks <= 1
        
        if not is_inc and not is_dec:
            return -1
            
        # Identify the target state that corresponds to [0, 1, ..., n-1]
        # Find position of 0 in nums
        pos0 = nums.index(0)
        
        # If cyclically increasing:
        # Rotating left pos0 times puts 0 at index 0 -> target is (0, pos0)
        # If cyclically decreasing:
        # Reversing puts it in increasing order -> target corresponds to type 1
        target_states = set()
        
        if is_inc:
            target_states.add((0, pos0))
            
        if is_dec:
            # When reversed, element originally at index i moves to n - 1 - i.
            # In reversed array, 0 is at index (n - 1 - pos0).
            target_states.add((1, (n - 1 - pos0) % n))
            
        # BFS to find shortest path from (0, 0) to any target state
        queue = deque([(0, 0, 0)])  # (type, shift, distance)
        visited = {(0, 0)}
        
        while queue:
            t, s, dist = queue.popleft()
            
            if (t, s) in target_states:
                return dist
                
            # Next state 1: Rotate Left
            next_l = (t, (s + 1) % n)
            if next_l not in visited:
                visited.add(next_l)
                queue.append((next_l[0], next_l[1], dist + 1))
                
            # Next state 2: Reverse
            next_r = (1 - t, (n - s) % n)
            if next_r not in visited:
                visited.add(next_r)
                queue.append((next_r[0], next_r[1], dist + 1))
                
        return -1