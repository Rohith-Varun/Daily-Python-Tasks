import heapq
from typing import List
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        # Build adjacency list: u -> list of (v, w)
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))          
        # Min-heap stores: (dist, node, consecutive_count)
        # Starting at node 0 with consecutive count 1 (since it has labels[0])
        pq = [(0, 0, 1)]      
        # Distance dictionary or 2D array to track minimum cost for state (node, count)
        # Using a dictionary for sparse state representation
        dist = {}
        dist[(0, 1)] = 0        
        while pq:
            d, u, count = heapq.heappop(pq)            
            # If we reached the destination node, return the distance
            if u == n - 1:
                return d            
            if d > dist.get((u, count), float('inf')):
                continue                
            for v, w in graph[u]:
                # Determine next consecutive count
                if labels[u] == labels[v]:
                    next_count = count + 1
                else:
                    next_count = 1                
                # Prune paths that exceed the maximum allowed consecutive identical characters
                if next_count > k:
                    continue              
                new_dist = d + w
                if new_dist < dist.get((v, next_count), float('inf')):
                    dist[(v, next_count)] = new_dist
                    heapq.heappush(pq, (new_dist, v, next_count))                  
        return -1
