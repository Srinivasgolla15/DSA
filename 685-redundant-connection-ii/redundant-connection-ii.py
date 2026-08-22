class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)

        # parent[v] = current parent of v
        parent = [0] * (n + 1)

        candidate1 = None
        candidate2 = None

        # -----------------------------------------
        # 1. Find node with two parents
        # -----------------------------------------
        for u, v in edges:

            if parent[v] == 0:
                parent[v] = u

            else:
                # v has two parents
                candidate1 = [parent[v], v]
                candidate2 = [u, v]

        # -----------------------------------------
        # 2. DSU
        # -----------------------------------------
        dsu = list(range(n + 1))

        def find(x):
            if dsu[x] != x:
                dsu[x] = find(dsu[x])
            return dsu[x]

        def union(a, b):
            ra = find(a)
            rb = find(b)

            if ra == rb:
                return False

            dsu[rb] = ra
            return True

        # -----------------------------------------
        # 3. Try removing candidate2
        # -----------------------------------------
        if candidate2:

            for u, v in edges:

                if [u, v] == candidate2:
                    continue

                if not union(u, v):
                    # Cycle still exists
                    # => candidate1 is the bad edge
                    return candidate1

            # Removing candidate2 fixes everything
            return candidate2

        # -----------------------------------------
        # 4. No two-parent node
        #    => simply find cycle edge
        # -----------------------------------------
        dsu = list(range(n + 1))

        for u, v in edges:

            if not union(u, v):
                return [u, v]
        
        