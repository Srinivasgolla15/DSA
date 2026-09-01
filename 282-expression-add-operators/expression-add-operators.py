class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """

# ----------Backtracking / DFS with Expression Evaluation------------
# Time: O(4^n)
# Space: O(n) recursion stack
#       + O(n * 4^n) for the returned expressions in the worst case
        # arr = []

        # def dfs(i, exp, curr, prev):

        #     if i == len(num):
        #         if curr == target:
        #             arr.append(exp)
        #         return

        #     for j in range(i, len(num)):

        #         # Don't allow numbers like 05, 00, 012
        #         if num[i] == "0" and j > i:
        #             break

        #         number = int(num[i:j + 1])

        #         # First number
        #         if i == 0:
        #             dfs(
        #                 j + 1,
        #                 str(number),
        #                 number,
        #                 number
        #             )

        #         else:
        #             # +
        #             dfs(
        #                 j + 1,
        #                 exp + "+" + str(number),
        #                 curr + number,
        #                 number
        #             )

        #             # -
        #             dfs(
        #                 j + 1,
        #                 exp + "-" + str(number),
        #                 curr - number,
        #                 -number
        #             )

        #             # *
        #             dfs(
        #                 j + 1,
        #                 exp + "*" + str(number),
        #                 curr - prev + prev * number,
        #                 prev * number
        #             )

        # dfs(0, "", 0, 0)

        # return arr


        ans = []
        choices = [[] for _ in range(len(num))]

        # Pre-generate all possible numbers
        for i in range(len(num)):
            curr = ""

            for j in range(i, len(num)):

                # Don't allow 05, 012, etc.
                if num[i] == "0" and j > i:
                    break

                curr += num[j]

                choices[i].append((j, int(curr)))

        def dfs(i, exp, curr, prev):

            # Base case
            if i == len(num):
                if curr == target:
                    ans.append(exp)
                return

            # Try every number that can start from i
            for j, number in choices[i]:

                # First number
                if i == 0:
                    dfs(
                        j + 1,
                        str(number),
                        number,
                        number
                    )

                else:
                    # +
                    dfs(
                        j + 1,
                        exp + "+" + str(number),
                        curr + number,
                        number
                    )

                    # -
                    dfs(
                        j + 1,
                        exp + "-" + str(number),
                        curr - number,
                        -number
                    )

                    # *
                    dfs(
                        j + 1,
                        exp + "*" + str(number),
                        curr - prev + prev * number,
                        prev * number
                    )

        dfs(0, "", 0, 0)

        return ans