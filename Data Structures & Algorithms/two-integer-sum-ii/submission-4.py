class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer = 0 # Starting pointer, left most
        right_pointer = len(numbers) - 1 # End pointer, right most

        # While pointers have not met
        while left_pointer < right_pointer:
            # If sum is less than target, move left most pointer
            if numbers[left_pointer] + numbers[right_pointer] < target:
                left_pointer += 1
            # If sum is greater than target, move right most pointer
            elif numbers[left_pointer] + numbers[right_pointer] > target:
                right_pointer -= 1
            # If none of the above conditions are met, sum must equal target so return indexes
            else:
                return[left_pointer + 1, right_pointer + 1]
        