class Solution(object):
    def verticalTraversal(self, root):
        """
        Approach: DFS + HashMap + Sorting

        TC: O(N log N)
        SC: O(N)
        """

        hm = {}
        res = []

        # Store (row, value) for each column
        def dfs(root, r, c):
            if not root:
                return

            if c not in hm:
                hm[c] = []

            hm[c].append((r, root.val))

            dfs(root.left, r + 1, c - 1)
            dfs(root.right, r + 1, c + 1)

        # Root starts at row 0, column 0
        dfs(root, 0, 0)

        # Process columns from left to right
        sort = sorted(hm.keys())

        for key in sort:
            # Sort by row, then by value
            hm[key].sort(key=lambda x: (x[0], x[1]))

            arr = []

            for i in hm[key]:
                arr.append(i[1])

            res.append(arr)

        return res