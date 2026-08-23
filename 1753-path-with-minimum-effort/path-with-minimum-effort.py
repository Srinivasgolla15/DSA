class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        




# ------------Dijkstra similar to 778 swim --------------
# time : O(mn log(mn))
# space : O(mn)


        m = len(heights)
        n = len(heights[0])

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        dist = [[float("inf")] * n for _ in range(m)]

        heap = []

        dist[0][0] = 0

        # (effort, row, col)
        heapq.heappush(heap, (0, 0, 0))

        while heap:

            curr, r, c = heapq.heappop(heap)

            if r == m-1 and c == n-1:
                return curr

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                # Difference for this edge
                diff = abs(heights[r][c] - heights[nr][nc])

                # Maximum difference encountered on this path
                new_effort = max(curr, diff)

                # Better path to this cell
                if new_effort < dist[nr][nc]:

                    dist[nr][nc] = new_effort

                    heapq.heappush(
                        heap,
                        (new_effort, nr, nc)
                    )

