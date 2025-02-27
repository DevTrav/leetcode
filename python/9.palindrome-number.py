#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
    # Compare with reverse
        if x < 0:
            return False
        
        original, reversed = x, 0
        while x != 0:
            reversed = reversed * 10 + x % 10
            x //= 10
        
        return original == reversed

    # Convert string and reverse
    # def isPalindrome(self, x: int) -> bool:
    #     x_str = str(x)

    #     return x_str == x_str[:: -1]
        
# @lc code=end

