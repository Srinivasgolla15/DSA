class Solution(object):
    def evalRPN(self, tokens):

        stack = []

        for token in tokens:

            if token not in "+-*/":
                stack.append(int(token))
                continue

            b = stack.pop()
            a = stack.pop()

            if token == "+":
                result = a + b

            elif token == "-":
                result = a - b

            elif token == "*":
                result = a * b

            else:
                result = abs(a) // abs(b)

                if (a < 0) != (b < 0):
                    result = -result

            stack.append(result)

        return stack[-1]