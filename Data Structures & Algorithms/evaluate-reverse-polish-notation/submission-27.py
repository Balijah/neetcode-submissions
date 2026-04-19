import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        operations = { 
                    "*" : operator.mul,
                    "+" : operator.add,
                    "-" : operator.sub,
                    "/" : operator.truediv
                    }

        # Loop through the tokens input
        for i in range(len(tokens)):
            # While the element is NOT an operator, add it to the numbers array
            if tokens[i] not in "+-*/":
                numbers.append(int(tokens[i]))
            # But if it IS an operator, stop and use that operator on the existing elements in the number array
            else:
                a = numbers.pop()
                b = numbers.pop()
                running_product = operations[tokens[i]](b, a)
                numbers.append(int(running_product))
        return numbers.pop(0)