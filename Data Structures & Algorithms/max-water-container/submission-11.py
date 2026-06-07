class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lefty = 0
        righty = len(heights) - 1
        res = 0

        while lefty < righty:
            area = (righty - lefty) * min(heights[lefty], heights[righty])
            res = max(res, area)
            if heights[lefty] < heights[righty]:
                lefty += 1
            elif heights[lefty] > heights[righty]:
                righty -= 1
            else:
                lefty += 1
                righty -= 1
        return res