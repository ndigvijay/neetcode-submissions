class Solution:
    def isValid(self, s: str) -> bool:
        valid_params = {"{":"}","[":"]","(":")"}
        if len(s)<2:
            return False
        left = 0
        right = len(s) - 1
        while(left<right):
            if valid_params[s[left]] != s[right]:
                return False
            else:
                left = left + 1
                right = right -1
        
        return True



        