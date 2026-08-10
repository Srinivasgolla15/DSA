 

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        # Count frequencies
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1

        # Max heap using negative frequencies
        heap = []
        for ch, count in freq.items():
            heapq.heappush(heap, (-count, ch))

        # (count, task, available_time)
        queue = deque()

        time = 0

        while heap or queue:

            # Move ready tasks back to heap
            while queue and queue[0][2] <= time:
                count, ch, available = queue.popleft()
                heapq.heappush(heap, (count, ch))

            # Execute highest-frequency task
            if heap:
                count, ch = heapq.heappop(heap)
                count += 1

                # Put back if tasks remain
                if count < 0:
                    queue.append((count, ch, time + n + 1))

            # One interval passes
            time += 1

        return time