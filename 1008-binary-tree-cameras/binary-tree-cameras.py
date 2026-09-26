class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

# ------------------ Greedy + Postorder DFS------------------
# TC: O(N)
# SC: O(H) recursion stack goes till height.
        # count = [0]

        # def dfs(root):
        #     if not root:
        #         return

        #     # First solve children
        #     dfs(root.left)
        #     dfs(root.right)

        #     # Leaf is uncovered
        #     if root.left is None and root.right is None:
        #         root.val = -1
        #         return

        #     # If any child is uncovered, put camera here
        #     if (root.left and root.left.val == -1) or \
        #        (root.right and root.right.val == -1):
        #         root.val = 2
        #         count[0] += 1

        #     # If any child has a camera, current node is covered
        #     elif (root.left and root.left.val == 2) or \
        #          (root.right and root.right.val == 2):
        #         root.val = 1

        #     # Otherwise current node is uncovered
        #     else:
        #         root.val = -1

        # dfs(root)

        # # If root is still uncovered, add camera
        # if root.val == -1:
        #     count[0] += 1

        # return count[0]


# ------------------ Greedy + Postorder DFS  simplified CHATGPT------------------
# TC: O(N)
# SC: O(H) recursion stack goes till height.

        count = [0]

        def dfs(root):
            if not root:
                return 2

            left = dfs(root.left)
            right = dfs(root.right)

            # If any child is uncovered, place camera here
            if left == 0 or right == 0:
                count[0] += 1
                return 1

            # If any child has a camera, current node is covered
            if left == 1 or right == 1:
                return 2

            # Both children are covered, but neither has a camera
            return 0

        # Root cannot be left uncovered
        if dfs(root) == 0:
            count[0] += 1

        return count[0]
