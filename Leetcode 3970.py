import heapq
from typing import List
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))          
        pq = [(0, 0, 1)]      
        dist = {}
        dist[(0, 1)] = 0        
        while pq:
            d, u, count = heapq.heappop(pq)            
            if u == n - 1:
                return d            
            if d > dist.get((u, count), float('inf')):
                continue                
            for v, w in graph[u]:
                if labels[u] == labels[v]:
                    next_count = count + 1
                else:
                    next_count = 1                
                if next_count > k:
                    continue              
                new_dist = d + w
                if new_dist < dist.get((v, next_count), float('inf')):
                    dist[(v, next_count)] = new_dist
                    heapq.heappush(pq, (new_dist, v, next_count))                  
        return -1
