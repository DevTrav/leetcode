/*
 * @lc app=leetcode id=704 lang=golang
 *
 * [704] Binary Search
 */

// @lc code=start

/*
 */
func search(nums []int, target int) int {

	start := 0
	end := len(nums) - 1

	for start <= end {
		mid := start + (end-start)/2

		if target == nums[mid] {
			return mid
		} else if target < nums[mid] {
			end = mid - 1
		} else if target > nums[mid] {
			start = mid + 1
		}
	}
	return -1
}

// @lc code=end

