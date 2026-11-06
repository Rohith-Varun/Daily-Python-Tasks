from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # Sort logs by their timestamps
        logs.sort(key=lambda x: x[1])
        
        # Pair each query with its original index so we can restore the original order
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
        
        ans = [0] * len(queries)
        l = 0
        r = 0
        server_counts = {}
        active_servers = 0
        
        for q_idx, q_time in sorted_queries:
            window_start = q_time - x
            window_end = q_time
            
            # Add logs that fall within the current window ending at window_end
            while r < len(logs) and logs[r][1] <= window_end:
                server_id = logs[r][0]
                if server_counts.get(server_id, 0) == 0:
                    active_servers += 1
                server_counts[server_id] = server_counts.get(server_id, 0) + 1
                r += 1
                
            # Remove logs that fall outside the window (before window_start)
            while l < len(logs) and logs[l][1] < window_start:
                server_id = logs[l][0]
                server_counts[server_id] -= 1
                if server_counts[server_id] == 0:
                    active_servers -= 1
                l += 1
                
            # Zero-request servers = Total servers (n) - Active servers in the window
            ans[q_idx] = n - active_servers
            
        return ans
