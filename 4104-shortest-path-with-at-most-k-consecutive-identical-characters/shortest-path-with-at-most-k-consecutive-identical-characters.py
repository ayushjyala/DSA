from typing import List
import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        # Build adjacency list
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            
        # Priority queue stores (weight, node, consecutive_count)
        pq = []
        
        # Initial state: starting at node 0, count is 1, weight sum is 0
        initial_count = 1
        heapq.heappush(pq, (0, 0, initial_count))
        
        # Best distance map: (node, count) -> minimum weight
        dist = {}
        dist[(0, initial_count)] = 0
        
        while pq:
            w, u, count = heapq.heappop(pq)
            
            # If we reached the destination node n - 1, return the total weight
            if u == n - 1:
                return w
                
            if w > dist.get((u, count), float('inf')):
                continue
                
            for v, weight in graph[u]:
                # Determine the new count of consecutive identical characters
                if labels[v] == labels[u]:
                    new_count = count + 1
                else:
                    new_count = 1
                    
                # If the consecutive count exceeds k, this path is invalid
                if new_count > k:
                    continue
                    
                next_w = w + weight
                
                if next_w < dist.get((v, new_count), float('inf')):
                    dist[(v, new_count)] = next_w
                    heapq.heappush(pq, (next_w, v, new_count))
                    
        return -1