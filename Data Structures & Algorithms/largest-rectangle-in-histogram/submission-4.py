class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        results = []

        for i in range(len(heights)):
            new_start_index = i
            while stack and heights[i] < stack[-1][0]:
                popped_bar = stack.pop()
                popped_bar_area = (i - popped_bar[1]) * popped_bar[0]
                results.append(popped_bar_area)
                new_start_index = popped_bar[1]
            stack.append((heights[i], new_start_index))

        for i in range(len(stack)):
            res = (len(heights) - stack[i][1]) * stack[i][0]
            results.append(res)
        
        return max(results)
