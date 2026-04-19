class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False
                
        if s[0] not in "{[(":
            return False
        
        while "()" in s or "{}" in s or "[]" in s:
            s = s.replace("()", '')
            s = s.replace("[]", '')
            s = s.replace("{}", '')
        return s == ''