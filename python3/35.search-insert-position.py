#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Initialize left and right pointers to slice array
        #start at the end of the input list nums
        # While loop continues as long as left<= right
        #Loop calculates mid
        # If nums[mid] = target, return mid
        #If nums[mid] < target, left pointer updated to mid + 1
        #Otherwise, if nums[mid] > target, target must be in the left half 
        #right pointer updated to mid - 1
        #If target not found, function returns left pointer which is the index the target would be in ascending order

        left, right = 0, len(nums) - 1

        while left <= right:
            mid =(left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid -1
        return left 
# @lc code=end

