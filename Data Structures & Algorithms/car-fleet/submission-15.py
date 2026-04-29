class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        n = len(position)
        cars = []

        for i in range(n):
            cars.append((position[i], speed[i]))

        cars.sort(reverse = True)
        
        iterations_to_target = []

        for i in range(n):
            iterations_to_target.append((target - cars[i][0]) / cars[i][1])
                
        for i in range(n):
            if not stack or stack[-1] < iterations_to_target[i]:
                stack.append(iterations_to_target[i])
        return(len(stack))