import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        # free_servers stores tuples of (weight, index)
        free_servers = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free_servers)
        
        # used_servers stores tuples of (free_time, weight, index)
        used_servers = []
        
        ans = []
        t = 0
        
        for j, task_duration in enumerate(tasks):
            t = max(t, j)
            
            # If no free servers exist, advance time to when the first busy server becomes free
            if not free_servers:
                t = used_servers[0][0]
            
            # Release all servers that finish by current time t
            while used_servers and used_servers[0][0] <= t:
                free_time, weight, idx = heapq.heappop(used_servers)
                heapq.heappush(free_servers, (weight, idx))
            
            # Pick the available server with the lowest (weight, index)
            weight, idx = heapq.heappop(free_servers)
            ans.append(idx)
            
            # Mark the server as busy until t + task_duration
            heapq.heappush(used_servers, (t + task_duration, weight, idx))
            
        return ans