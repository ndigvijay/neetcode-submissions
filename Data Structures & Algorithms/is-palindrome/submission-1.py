class Solution:
    def isPalindrome(self, s: str) -> bool:
        end = len(s)-1
        start = 0
        while(start<end):
            if not s[start].isalpha():
                start = start + 1
            if not s[end].isalpha():
                end = end - 1
            if s[start].lower() != s[end].lower():
                return False
            else:
                start = start + 1
                end = end - 1
        return True
        