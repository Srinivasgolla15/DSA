class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
          # Step 1: Build graph and indegree
        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        # Step 2: Put all courses with indegree 0 into queue
        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        order = []
        # completed = 0

        # Step 3: BFS (Topological Sort)
        while queue:

            course = queue.popleft()

            # completed += 1
            order.append(course)

            for neighbor in graph[course]:

                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: Check for cycle
        if len(order) == numCourses:
            return order

        return []

# Time Complexity: O(V + E)
# V = number of courses
# E = number of prerequisite pairs
#
# - Build graph: O(E)
# - Build indegree array: O(E)
# - Initialize queue: O(V)
# - BFS Topological Sort: O(V + E)
#
# Space Complexity: O(V + E)
# - Graph: O(V + E)
# - Indegree array: O(V)
# - Queue: O(V)
# - Order array: O(V)
        