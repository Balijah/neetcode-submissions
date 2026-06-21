class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left_array = []
        right_array = []
        res = 0

        for i in range(len(height)):
            if not left_array:
                left_array.append(height[i])
            else:
                left_array.append(max(left_array[-1], height[i]))
        
        for i in range(len(height) - 1, -1, - 1):
            if not right_array:
                right_array.append(height[i])
            else:
                right_array.append(max(right_array[-1], height[i]))

        right_array = right_array[::-1]
        print(right_array)
        
        for i in range(len(height)):
            total_water = min(left_array[i], right_array[i]) - height[i]
            res += total_water
        
        return res
