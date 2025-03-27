#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        #Initialize lesft as 0
        # Intialize right as len(letters)-1
        res = "zz"
        left, right = 0, len(letters) -1

        #
        while left <= right:
        #   Compute middle as (left + right) //2
            pivot = (right + left ) // 2
            if letters[pivot] <= target:
                left = pivot + 1
            else:
                if res > letters[pivot]:
                    res = letters[pivot]
                right = pivot - 1

        return res if res != "zz" else letters[0]

        #       Update right to middle -1
        #   Else:
        #       Update left to middle + 1
        #If left >= length of letters, set left to 0
        #
        #Return letters[left] as the smallest character greater than target
# @lc code=end

