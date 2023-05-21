"""

Problem: https://leetcode.com/problems/excel-sheet-column-number/

Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnTitle = "A"
Output: 1

Example 2:

Input: columnTitle = "AB"
Output: 28

Example 3:

Input: columnTitle = "ZY"
Output: 701

"""

class Solution:
    
    def titleToNumber(self, columnTitle):
        
        res = 0
        i = len(columnTitle) - 1
        m = 1

        while i >= 0:

            value = ord(columnTitle[i]) - ord('A') + 1

            res += value * m
            m = m * 26

            i -= 1

        return res
    
"""

A note on powers:

# alphabets

26^0 = 0
26^1 = 26
26^2 = 676

_ _ _
676 26 0

# decimal

10^0 = 0
10^1 = 10
10^2 = 100

_ _ _
100 10 0

# binary

2^0 = 0
2^1 = 2
2^2 = 4
2^3 = 8

_ _ _ _
8 4 2 0

"""

"""

What is len(s)-i-1 ?

x = len(s) - i - 1
len(s) == 4:

i    x
0    3
1    2
2    1
3    0

"""

