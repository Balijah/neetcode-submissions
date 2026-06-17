class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        res = 0

        for i in range(1, len(height) - 1):
            right = max(height[i:])
            left = max(height[:i])

            print(left)
            print(right)
            print(min(left, right))
            print(res)

            total_water = min(left, right) - height[i]

            if total_water > 0:
                res += total_water
        
        return res

