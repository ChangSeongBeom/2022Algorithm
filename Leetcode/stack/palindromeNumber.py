class Solution:
    def isPalindrome(self, x: int) -> bool:
        strList = str(x)
        reversedList = list(reversed(strList))

        if strList == ''.join(reversedList):
            return True
        else:
            return False