class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        heap = []
        dist = [[float("inf")]*n for _ in range(n)]
        
        dist[0][0] = grid[0][0]
        heapq.heappush(heap,(grid[0][0],0,0))
        
        while heap:
            curr, i ,j = heapq.heappop(heap)

            if i == n-1 and j == n-1:
                return curr
            
            for r,c in directions:
                nr,nc = r+i,c+j

                if nr<0 or nr>n-1 or nc<0 or nc>n-1:
                    continue

                newtime = max(curr,grid[nr][nc])

                if newtime < dist[nr][nc]:
                    dist[nr][nc] = newtime

                    heapq.heappush(heap,(newtime,nr,nc))

            


        