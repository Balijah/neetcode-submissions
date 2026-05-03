class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''

        for character in s:
            if character.isalnum() == True:
                string += character

        if string.lower() == string[::-1].lower():
            return True
        return False
        
        