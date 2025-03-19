/*
 * @lc app=leetcode id=35 lang=golang
 *
 * [35] Search Insert Position
 */

// @lc code=start
func searchInsert(nums []int, target int) int {

	beg := 0
	end := len(nums) - 1

	for beg <= end {
		mid := beg + (end-beg)/2

		if nums[mid] == target {
			return mid
		} else if target < nums[mid] {

		} else {
			beg = mid + 1
		}
	}
	return nums[beg]
}

// @lc code=end

