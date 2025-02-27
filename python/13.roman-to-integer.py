#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary mapping Roman numerals to their values
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Iterate through the string from right to left
        for char in reversed(s):
            curr_value = roman_values[char]
            
            # If current value is greater than or equal to previous value, add it
            # Otherwise subtract it (handles cases like IV, IX, XL, etc.)
            if curr_value >= prev_value:
                total += curr_value
            else:
                total -= curr_value
                
            prev_value = curr_value
            
        return total

# @lc code=end

