import heapq
class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        available = [(servers[i], i) for i in range(len(servers))]
        heapq.heapify(available)
        unavailable = []
        ans = []
        t = 0
        for j, task_time in enumerate(tasks):
            t = max(t, j)
            if not available and unavailable[0][0] > t:
                t = unavailable[0][0]
            while unavailable and unavailable[0][0] <= t:
                free_time, weight, index = heapq.heappop(unavailable)
                heapq.heappush(available, (weight, index))
            weight, index = heapq.heappop(available)
            ans.append(index)
            heapq.heappush(unavailable, (t + task_time, weight, index))
        return ans
