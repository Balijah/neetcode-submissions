class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        if len(s) % 2 != 0:
            return False
                
        if s[0] not in "{[(":
            return False
            
        for i in range(len(s)):
            if s[i] in "([{":
                stack.append(s[i])
                continue
            if s[i] == ")" and len(stack) != 0 and stack.pop() == "(":
                continue
            if s[i] == "]" and len(stack) != 0 and stack.pop() == "[":
                continue
            if s[i] == "}" and len(stack) != 0 and stack.pop() == "{":
                continue
            return False
        
        if len(stack) == 0:
            return True
        return False
        