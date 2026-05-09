class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer = 0 # Starting pointer, left most
        right_pointer = len(numbers) - 1 # End pointer, right most

        # While pointers have not met
        while left_pointer < right_pointer:
            # If the sum of two pointers is LESS THAN the target, move the left pointer inward
            while left_pointer < right_pointer and numbers[left_pointer] + numbers[right_pointer] < target:
                left_pointer += 1
            # If the sum of two pointers is GREATER THAN the target, move the right pointer inward
            while left_pointer < right_pointer and numbers[left_pointer] + numbers[right_pointer] > target:
                right_pointer -= 1
            # If the two pointers sum equal the target, return the index (1-indexed array)
            if numbers[left_pointer] + numbers[right_pointer] == target:
                return [left_pointer + 1, right_pointer + 1]
        