class Solution:
    def isValid(self, s: str) -> bool:
        
        parantheses = {")": "(", "}": "{", "]": "["}
        stack = []
        
        for char in s:
            if char in parantheses:
                top = stack.pop() if stack else '#'
                
                if parantheses[char] != top:
                    return False
            else:
                stack.append(char)
    
        return len(stack) == 0
