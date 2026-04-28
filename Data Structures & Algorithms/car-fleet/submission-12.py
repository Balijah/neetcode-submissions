class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        stack = []
        iterations_to_target = []
        cars = []

        for i in range(n):
            cars.append((position[i], speed[i]))
        
        cars.sort(reverse = True)
        
        for i in range(n):
            iterations = (target - cars[i][0]) / cars[i][1]
            iterations_to_target.append(iterations)
        
        for i in range(len(iterations_to_target)):
            if not stack or stack[-1] < iterations_to_target[i]:
                stack.append(iterations_to_target[i])  
        return len(stack)