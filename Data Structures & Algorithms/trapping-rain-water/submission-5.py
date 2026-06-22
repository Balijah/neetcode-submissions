class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        left_array = []
        right_array = [0] * n
        res = 0

        for i in range(len(height)):
            if not left_array:
                left_array.append(height[i])
            else:
                left_array.append(max(left_array[-1], height[i]))
        
        for i in range(len(height) - 1, -1, -1):
            if i == n - 1:
                right_array[i] = height[i]
            else:
                right_array[i] = max(right_array[i + 1], height[i])

        for i in range(n):
            total_water = min(left_array[i], right_array[i]) - height[i]
            res += total_water
        
        return res