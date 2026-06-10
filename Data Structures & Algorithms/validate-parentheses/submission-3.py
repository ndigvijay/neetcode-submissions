class Solution:
    def isValid(self, s: str) -> bool:
        valid_params = {"}":"{","]":"[",")":"("}
        if len(s)<2:
            return False
        stack=[]
        for i in s:
            if i =="{" or i == "(" or i =="[":
                stack.append(i)
            elif valid_params[i] == stack[-1]:
                stack.pop()
        
        if len(stack) == 0:
            return True



        