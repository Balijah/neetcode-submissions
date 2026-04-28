class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)

        cars = []

        for i in range(n):
            cars.append((position[i], speed[i]))

        # Sort by position from lowest to highest
        cars.sort(reverse = True)

        stack = []

        # Go from closest to target to farthest from target
        for i in range(n):
            pos, spd = cars[i]
            time_to_target = (target - pos) / spd

            # If this car takes longer than the fleet ahead,
            # it cannot catch up, so it forms a new fleet.
            if not stack or time_to_target > stack[-1]:
                stack.append(time_to_target)

            # Otherwise, it catches up to the fleet ahead,
            # so we do nothing.

        return len(stack)