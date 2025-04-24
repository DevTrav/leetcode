#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Create HashMap to store number and their indicies
        numsMap = {}

        for i, num in enumerate(nums): 
            compliment = target - num

            if compliment in numsMap:
                return [numsMap[compliment], i]
            numsMap[num] = i

        return []

        
        
# @lc code=end

