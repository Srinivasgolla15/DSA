class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # Time Complexity: O(n² × n!)
        #
        # Explanation:
        # 1. There are n! permutations.
        # 2. For each recursive call, we loop through all n elements.
        # 3. Checking "nums[i] not in arr" takes O(n) because 'arr' is a list.
        # 4. Therefore, each recursive level performs O(n²) work.
        # 5. Overall Time = O(n² × n!)
        #
        # Auxiliary Space: O(n)
        # - O(n) recursion stack.
        # - O(n) for the current permutation (arr).
        #
        # Output Space: O(n × n!)
        # - We store n! permutations, each of length n.

        # Stores all permutations
        res = []

        # arr = current permutation being built
        def dfs(arr):

            # Base Case:
            # If current permutation contains all numbers,
            # make a copy and store it.
            if len(arr) == len(nums):
                res.append(arr[:])      # O(n) copy
                return

            # Try every number as the next choice
            for i in range(len(nums)):     # O(n)

                # Membership check in a list is O(n)
                if nums[i] not in arr:

                    # -------- Choose --------
                    arr.append(nums[i])

                    # -------- Explore --------
                    dfs(arr)

                    # -------- Undo (Backtrack) --------
                    arr.pop()

        # Start with an empty permutation
        dfs([])

        return res