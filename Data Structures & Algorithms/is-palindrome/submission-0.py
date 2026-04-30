class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_s = ''
        
        for character in s:
            if character.isalnum() == True:
                new_s += character
        
        if new_s.lower() == new_s[::-1].lower():
            return True
        return False