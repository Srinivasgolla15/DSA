class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        # using dijkstra's algorithm , using heap and distance array 
        graph={i:[] for i in range(1,n+1)}
        for i in range(len(times)):
            ele=times[i][0]
            graph[ele].append(times[i][1:])
        
        dist=[float("inf")]*(n+1)

        dist[k]=0

        heap=[(0,k)]
        while heap:
            curr_time,node = heapq.heappop(heap)
            if curr_time > dist[node]:
                continue
            for nei,time in graph[node]:
                next_time = curr_time + time
                if next_time< dist[nei]:
                    dist[nei] = next_time
                    heapq.heappush(heap,(next_time,nei))
        max1=float("-inf")
        for i in range(1,len(dist)):
            if dist[i]==float("inf"):
                return -1
            max1=max(dist[i],max1)
        return max1
        
            


        
        
        