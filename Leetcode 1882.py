import heapq
class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        # Min-heap for available servers: stores (weight, index)
        available = [(servers[i], i) for i in range(len(servers))]
        heapq.heapify(available)
        
        # Min-heap for unavailable servers: stores (free_time, weight, index)
        unavailable = []
        ans = []
        t = 0
        for j, task_time in enumerate(tasks):
            # Time cannot be less than the current task arrival time
            t = max(t, j)
            
            # If no servers are available, fast-forward time to when the next server frees up
            if not available and unavailable[0][0] > t:
                t = unavailable[0][0]
            
            # Release all servers that become free by time t
            while unavailable and unavailable[0][0] <= t:
                free_time, weight, index = heapq.heappop(unavailable)
                heapq.heappush(available, (weight, index))
            
            # Assign the task to the best available server
            weight, index = heapq.heappop(available)
            ans.append(index)
            
            # Push the server to unavailable with its release time
            heapq.heappush(unavailable, (t + task_time, weight, index))
            
        return ans
