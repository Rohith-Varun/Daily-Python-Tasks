import bisect
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        busy_servers = []  # Min-heap storing (release_time, server_id)
        available_servers = list(range(k))  # Sorted list acting as an ordered set of available servers
        request_count = [0] * k
        
        for j, (arr, ld) in enumerate(zip(arrival, load)):
            # Free up servers whose tasks are completed by the current arrival time
            while busy_servers and busy_servers[0][0] <= arr:
                _, server_id = heapq.heappop(busy_servers)
                # Insert back maintaining sorted order
                idx = bisect.bisect_left(available_servers, server_id)
                available_servers.insert(idx, server_id)
            
            if not available_servers:
                # All servers are busy, drop this request
                continue
            
            # Find the preferred starting server index (j % k)
            preferred = j % k
            idx = bisect.bisect_left(available_servers, preferred)
            
            if idx == len(available_servers):
                # Wrap around to the beginning of the available servers list
                server_id = available_servers.pop(0)
            else:
                server_id = available_servers.pop(idx)
            
            # Assign the request to the chosen server
            request_count[server_id] += 1
            heapq.heappush(busy_servers, (arr + ld, server_id))
            
        max_requests = max(request_count)
        return [i for i, count in enumerate(request_count) if count == max_requests]
