#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(first) :
            res = - 1
            l, r = 0, len(nums) - 1
            while l <= r:
                p = (l + r) // 2
                if nums[p] == target :
                    res = p
                    if first:
                        r = p - 1 
                    else:
                        l = p + 1
                elif nums[p] < target:
                    l = p + 1
                else:
                    r = p - 1
            return res
        first = search(True)
        if first == -1:
            return [-1, -1]
        last = search(False)
        return [first, last]

# @lc code=end

