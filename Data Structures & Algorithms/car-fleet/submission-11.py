class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Save n as variable
        n = len(position)

        # Create a stack
        stack = []

        # Create an array to hold iterations until each car reaches target
        iterations_to_target = []

        # Create an array of each car that will hold each car's (position, speed)
        cars = []

        # Create an ordered pair of (position, speed)
        for i in range(n):
            cars.append((position[i], speed[i]))
        
        # Sort each car by the position it is in from lowest to highest
        cars.sort()
        
        # Calculate how many iterations each car will take to reach target
        for i in range(n):
            iterations = (target - cars[i][0]) / cars[i][1]
            iterations_to_target.append(iterations)
        
        # Go through iterations_to_target
        for i in range(len(iterations_to_target) - 1, -1, -1):
            # While stack is non empty and top of stack is greater than what we are currently looking at (iterations_to_target[i]), then stack.pop()
            if not stack or stack[-1] < iterations_to_target[i]:
                stack.append(iterations_to_target[i])  
            # If stack is empty or stack[-1] < iterations_to_target[i] then add to the stack
        # Return number of fleets
        return len(stack)