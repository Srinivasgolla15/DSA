class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
# ------------------Recursive/Innermost Parentheses Reduction------

# time : O(n*n)
# space : O(n)

        # if not s:
        #     return 0

        # # Evaluate expression without parentheses
        # def evalu(string):

        #     total = 0
        #     sign = 1
        #     num = ""

        #     i = 0

        #     while i < len(string):

        #         ch = string[i]

        #         if ch == " ":
        #             i += 1
        #             continue

        #         if ch.isdigit():
        #             num += ch

        #         elif ch == "+" or ch == "-":

        #             # Unary + or -
        #             j = i - 1
        #             while j >= 0 and string[j] == " ":
        #                 j -= 1

        #             if j < 0 or string[j] in "+-":

        #                 if ch == "-":
        #                     sign *= -1

        #             else:
        #                 if num:
        #                     total += sign * int(num)

        #                 if ch == "+":
        #                     sign = 1
        #                 else:
        #                     sign = -1

        #                 num = ""

        #         i += 1

        #     if num:
        #         total += sign * int(num)

        #     return total

        # # Evaluate inside one pair of parentheses
        # def rec(string, start, end):
        #     return evalu(string[start + 1:end])

        # # Reduce one innermost parenthesis
        # def isParan(string):

        #     stack = []

        #     for i in range(len(string)):

        #         if string[i] == "(":
        #             stack.append(i)

        #         elif string[i] == ")" and stack:

        #             start = stack.pop()
        #             end = i

        #             value = rec(string, start, end)

        #             # Replace "(...)" with its value
        #             string = string[:start] + str(value) + string[end + 1:]

        #             return string

        #     return string

        # while "(" in s:
        #     s = isParan(s)

        # return evalu(s)


# ---------------Stack Simulation O(n) O(n)-----------------------

        if not s:
            return 0

        stack = []

        curr = 0
        num = ""
        sign = 1

        for ch in s:

            if ch == " ":
                continue

            # Build number
            elif ch.isdigit():
                num += ch

            # Finish current number, then set sign
            elif ch == "+":
                if num:
                    curr += sign * int(num)
                    num = ""

                sign = 1

            elif ch == "-":
                if num:
                    curr += sign * int(num)
                    num = ""

                sign = -1

            # Save current expression before '('
            elif ch == "(":
                stack.append((curr, sign))

                curr = 0
                sign = 1
                num = ""

            # Finish expression inside parentheses
            elif ch == ")":

                if num:
                    curr += sign * int(num)
                    num = ""

                # Restore expression before '('
                prev, prevsign = stack.pop()

                # Combine:
                # previous expression + sign * expression inside ()
                curr = prev + prevsign * curr

                sign = 1

        # Process final number
        if num:
            curr += sign * int(num)

        return curr