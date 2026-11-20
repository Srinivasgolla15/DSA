

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):

# ------------------DFS with dp O((V + E) × K) O(V × K)------------
          # Build graph
        graph = defaultdict(list)

        for u, v, price in flights:
            graph[u].append((v, price))

        memo = {}

        def dfs(city, flightsLeft):

            # ---------------- BASE CASE ----------------

            # Destination reached
            if city == dst:
                return 0

            # No flights left
            if flightsLeft == 0:
                return float("inf")

            # Already computed
            if (city, flightsLeft) in memo:
                return memo[(city, flightsLeft)]

            ans = float("inf")

            # Try every outgoing flight
            for nei, price in graph[city]:
                ans = min(ans, price + dfs(nei, flightsLeft - 1))

            memo[(city, flightsLeft)] = ans
            return ans

        answer = dfs(src, k + 1)

        return answer if answer != float("inf") else -1
# ---------------DIJKSTRA + min heap------------

        # Build adjacency list
        # u -> (v, cost)
        # graph = {i: [] for i in range(n)}

        # for u, v, w in flights:
        #     graph[u].append((v, w))

        # # Min heap stores:
        # # (total_price, current_node, stops_used)
        # heap = [(0, src, 0)]

        # # Stores minimum price for:
        # # (node, stops_used)
        # price = {}

        # while heap:

        #     # Get cheapest current path
        #     curr_price, node, stops = heapq.heappop(heap)

        #     # If destination reached
        #     # this is the cheapest valid answer
        #     if node == dst:
        #         return curr_price

        #     # If stops exceed limit
        #     # skip this path
        #     if stops > k:
        #         continue

        #     # Traverse neighbors
        #     for nei, cost in graph[node]:

        #         # Total new cost
        #         new_price = curr_price + cost

        #         # Process only if:
        #         # 1. state not visited before
        #         # OR
        #         # 2. found cheaper cost
        #         if ((nei, stops) not in price or
        #             new_price < price[(nei, stops)]):

        #             # Update best price
        #             price[(nei, stops)] = new_price

        #             # Push into heap
        #             heapq.heappush(
        #                 heap,
        #                 (new_price, nei, stops + 1)
        #             )

        # # Destination unreachable
        # return -1
# Time Complexity:
        # Building graph = O(E)
        #
        # State = (node, stops)
        # Each node can be visited for up to (k+1) stop counts
        # Total states = O(V*K)
        #
        # Each state may push edges into heap
        # Heap operations cost O(log(V*K))
        #
        # Overall:
        # O(E*K*log(V*K))
        #
        # Space Complexity:
        # Graph = O(E)
        # Heap = O(V*K)
        # Price dictionary = O(V*K)
        #
        # Overall:
        # O(E + V*K)


# ---------------Bellman-Ford (Bottom-Up DP) --------------
#         INF = float("inf")

#         # Cost to reach every city
#         dp = [INF] * n
#         dp[src] = 0

#         # Relax all edges k+1 times
#         for _ in range(k + 1):

#             # Copy previous row
#             temp = dp[:]

#             for u, v, price in flights:

#                 if dp[u] == INF:
#                     continue

#                 temp[v] = min(temp[v], dp[u] + price)

#             dp = temp

#         return -1 if dp[dst] == INF else dp[dst]

# # O(K × E)
# O(v)