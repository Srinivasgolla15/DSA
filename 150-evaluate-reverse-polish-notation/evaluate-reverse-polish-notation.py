class Solution(object):
    def evalRPN(self, tokens):

        stack = []

        for token in tokens:

            # If token is a number
            if token not in "+-*/":
                stack.append(int(token))

            else:
                # IMPORTANT:
                # b is the second operand
                # a is the first operand
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    result = a + b

                elif token == "-":
                    result = a - b

                elif token == "*":
                    result = a * b

                elif token == "/":
                    # Truncate toward zero
                    result = int(float(a) / b)

                stack.append(result)

        return stack[-1]