class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while len(stack) != 0 and stack[-1][0] < temperatures[i]:
                popped_value = stack.pop()
                diff = i - popped_value[1]
                res[popped_value[1]] = diff
            stack.append((temperatures[i], i))
            print(stack)
            print(res)
        return res