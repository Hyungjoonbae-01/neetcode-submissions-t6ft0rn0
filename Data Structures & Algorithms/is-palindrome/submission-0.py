class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1 = "".join(char.lower() for char in s if char.isalnum())
        if len(str1) == 0:
            return True
        
        for i in range(len(str1) // 2):
            if(str1[i] != str1[len(str1)-1-i]):
                return False
        return True



            
        