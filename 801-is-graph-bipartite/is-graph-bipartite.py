
class Solution(object):
    def isBipartite(self, graph):

# ---------------Wrong approach ------------------------
        # seta = set()
        # setb = set()

        # for i, nodes in enumerate(graph):

        #     if i in seta:
        #         for j in nodes:
        #             if j in seta:
        #                 return False
        #             setb.add(j)

        #     elif i in setb:
        #         for j in nodes:
        #             if j in setb:
        #                 return False
        #             seta.add(j)

        #     else:
        #         seta.add(i)

        #         for j in nodes:
        #             if j in seta:
        #                 return False
        #             setb.add(j)

        # return True


# -------------------------BFS correct approach---------------------
# Time: \(O(V+E)\) — every vertex and edge is processed at most a constant number of times.
# Space: \(O(V)\) — two sets and the BFS queue.
        from collections import deque

        seta = set()
        setb = set()

        for i in range(len(graph)):

            # Skip nodes already assigned to a group
            if i in seta or i in setb:
                continue

            # Start a new disconnected component
            seta.add(i)
            dq = deque([i])

            while dq:
                node = dq.popleft()

                if node in seta:
                    current = seta
                    opposite = setb
                else:
                    current = setb
                    opposite = seta

                for nei in graph[node]:

                    # Neighbor in the same group = conflict
                    if nei in current:
                        return False

                    # Assign unvisited neighbor to opposite group
                    if nei not in opposite:
                        opposite.add(nei)
                        dq.append(nei)

        return True

