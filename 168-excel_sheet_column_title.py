"""
Problem:

Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 

"""

class Solution:

    def convertToTitle(self, columnNumber):

        while columnNumber:
            columnNumber -= 1
            res = chr((columnNumber%26) + 65) + res
            columnNumber // 26

        return res
    
        # Notes:

        # ------------------

        # 1%26 = 1
        # 1 + 64 = 65 => chr(65) = 'A'

        # ------------------

        # 28%26 = 2
        # 2 + 64 = 66 => chr(66) = 'B'

        # 28//26 = 1
        # 1%26 = 1
        # 1 + 64 = 65 => chr(65) = 'A'

        # ans = 'BA'
        # Reversed = ans[::-1]

        # ------------------

        # 701%26 = 25
        # 25 + 64 = 89 => chr(89) = 'Y'
        
        # 701//26 = 26
        # 26%26 = 0
        # 0 + 64 = 64 => chr(64) = '@'
        
        # This is incorrect because it results in '@', whereas correct is 'Z'.

        # ------------------

        # The correct approach is to subtract 1 before the modulus:

        # 701-1 = 700
        # 700%26+65 = 89 => chr(89) = 'Y'
        # 700//26 = 26

        # 26-1 = 25
        # 25%26+65 = 90 => chr(90) = 'Z'