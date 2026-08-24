class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
# ---------------wRONG ANSWER DONT WORKOUt --------------- 
# ----------------graph + ticket ID + visited set + BFS/greedy------
        # graph = defaultdict(list)
        # n = len(tickets)
        # for i in range(n):
        #     u, v = tickets[i]
        #     graph[u].append((v, i))

        # queue = deque(["JFK"])
        # visited = set()
        # arr = []

        # while queue:

        #     origin = queue.popleft()
        #     arr.append(origin)
        #     nxt = None

        #     for dest in graph[origin]:

        #         if dest[1] not in visited:

        #             if nxt is None or dest[0] < nxt[0]:
        #                 nxt = dest

        #     if nxt is not None:

        #         visited.add(nxt[1])

        #         queue.append(nxt[0])

        # return arr


# ----------------- DFS + BACKTRACKING (TLE)---------------
# Time = O(E!)
# Space = O(E)

        # graph = defaultdict(list)

        # # Build graph
        # # Store (destination, ticket_id)
        # for i, (u, v) in enumerate(tickets):
        #     graph[u].append((v, i))

        # # Lexicographical order
        # for airport in graph:
        #     graph[airport].sort()

        # used = set()
        # path = ["JFK"]

        # def dfs(current):

        #     # Used all tickets
        #     if len(used) == len(tickets):
        #         return True

        #     # Try every unused ticket from current airport
        #     for destination, ticket_id in graph[current]:

        #         if ticket_id in used:
        #             continue

        #         # Choose
        #         used.add(ticket_id)
        #         path.append(destination)

        #         # Explore
        #         if dfs(destination):
        #             return True

        #         # Backtrack / undo
        #         path.pop()
        #         used.remove(ticket_id)

        #     return False

        # dfs("JFK")

        # return path

# --------------------Hierholzer + Sorting------------
        graph = defaultdict(list)

        # Build graph
        for u, v in tickets:
            graph[u].append(v)

        # Sort destinations lexicographically
        for airport in graph:
            graph[airport].sort(reverse=True)

        result = []

        def dfs(airport):

            # Keep consuming available tickets
            while graph[airport]:

                # Smallest destination
                next_airport = graph[airport].pop()

                dfs(next_airport)

            # Add while backtracking
            result.append(airport)

        dfs("JFK")

        # We constructed it backwards
        return result[::-1]

# Time:  O(E log E)  # Sorting all adjacency lists
# Space: O(E + V)    # Graph + result + recursion  


