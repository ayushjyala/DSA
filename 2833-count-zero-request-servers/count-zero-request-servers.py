from typing import List
from collections import defaultdict

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # Sort logs by time
        logs.sort(key=lambda item: item[1])
        
        # Store queries with their original indices: (query_time, original_index)
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])
        
        ans = [0] * len(queries)
        cnt = defaultdict(int)  # Tracks frequency of requests for each server in the current window
        active_servers = 0
        
        left = 0
        right = 0
        num_logs = len(logs)
        
        for q_time, original_idx in sorted_queries:
            window_start = q_time - x
            window_end = q_time
            
            # Expand right bound to include logs <= window_end
            while right < num_logs and logs[right][1] <= window_end:
                server_id = logs[right][0]
                if cnt[server_id] == 0:
                    active_servers += 1
                cnt[server_id] += 1
                right += 1
            
            # Shrink left bound to exclude logs < window_start
            while left < num_logs and logs[left][1] < window_start:
                server_id = logs[left][0]
                cnt[server_id] -= 1
                if cnt[server_id] == 0:
                    active_servers -= 1
                left += 1
            
            # Servers with 0 requests = total servers - servers with >= 1 request
            ans[original_idx] = n - active_servers
            
        return ans