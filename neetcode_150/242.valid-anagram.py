#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !=  len(t):
            return False
        s_dict = Counter(s)
        t_dict = Counter(t)

        return s_dict == t_dict #compare character count

        
# @lc code=end

