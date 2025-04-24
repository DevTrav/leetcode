#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen: # check if element is in the HasSet
                return True # duplicate found
            seen.add(num) # add element to HashSet
        return False # no duplicates found
        
# @lc code=end

