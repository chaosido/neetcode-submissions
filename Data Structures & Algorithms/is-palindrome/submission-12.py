class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([c for c in s if c.isalnum()]).lower()
        if len(s) <= 1:
            return True
        is_uneven = (len(s) % 2) == 1
        left = 0
        right = len(s) - 1  
        for i in range(len(s)):
            
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
            if left >= right:
                return True

        return False
