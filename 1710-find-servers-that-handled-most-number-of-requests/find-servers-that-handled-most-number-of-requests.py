from heapq import heappop, heappush
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        # Keeps track of available server IDs
        available = SortedList(range(k))
        
        # Min-heap storing (free_time, server_id) for busy servers
        busy = []
        
        # Array to count requests handled by each server
        count = [0] * k
        
        for i, (start, duration) in enumerate(zip(arrival, load)):
            # 1. Free up servers whose tasks are finished by current start time
            while busy and busy[0][0] <= start:
                _, server_id = heappop(busy)
                available.add(server_id)
            
            # 2. If no available servers, drop the request
            if not available:
                continue
            
            # 3. Find the first available server >= (i % k)
            target = i % k
            idx = available.bisect_left(target)
            
            # If no server >= target, wrap around to the first available server
            if idx == len(available):
                idx = 0
            
            server_id = available.pop(idx)
            
            # 4. Assign request to the chosen server
            count[server_id] += 1
            heappush(busy, (start + duration, server_id))
        
        # Find all servers with maximum handled requests
        max_req = max(count)
        return [i for i in range(k) if count[i] == max_req]