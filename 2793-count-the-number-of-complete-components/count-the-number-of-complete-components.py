class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        # graph ={i:[] for i in range(n)}

        # for u, v in edges:
        #     graph[u].append(v)
        #     graph[v].append(u)
        # visited=set()
        # complete_count=0

        # def dfs(node):
        #     stack =[node]
        #     nodes = []
        #     visited.add(node)

        #     while stack:
        #         curr= stack.pop()
        #         nodes.append(curr)

        #         for nei in graph[curr]:
        #             if nei not in visited:
        #                 visited.add(nei)
        #                 stack.append(nei)

        #     return nodes

        # for i in range(n):
        #     if i not in visited:
        #         component = dfs(i)

        #         k = len(component)

        #         edge_count = 0
        #         for node in component:
        #             edge_count += len(graph[node])

        #         edge_count //= 2

        #         if edge_count == k * (k - 1) // 2:
        #             complete_count += 1

        # return complete_count


# BFS APPROACH ----------------------------------------

        # Build graph
        graph = {i: [] for i in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        complete_components = 0

        def bfs(start):

            q = deque([start])
            visited.add(start)

            nodes = 0
            edge_count = 0

            while q:

                node = q.popleft()

                # Count current node
                nodes += 1

                for nei in graph[node]:

                    # Count every adjacency-list edge
                    edge_count += 1

                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)

            # Undirected graph counts every edge twice
            actual_edges = edge_count // 2

            # Complete graph formula
            required_edges = nodes * (nodes - 1) // 2

            return actual_edges == required_edges

        # Find all connected components
        for node in range(n):

            if node not in visited:

                if bfs(node):
                    complete_components += 1

        return complete_components
# Time Complexity:
# O(V + E)
#
# Every node is visited once.
# Every edge is processed twice
# (once from each endpoint).

# Space Complexity:
# O(V + E)
#
# Graph: O(V + E)
# Visited Set: O(V)
# Queue: O(V)



        