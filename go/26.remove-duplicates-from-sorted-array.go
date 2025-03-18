/*
 * @lc app=leetcode id=26 lang=golang
 *
 * [26] Remove Duplicates from Sorted Array
 */

// @lc code=start
//for loop solution
// func removeDuplicates(nums []int) int {
// 	for i := 1; i < len(nums); i++ {
// 		if nums[i] == nums[i-1] {
// 			nums = append(nums[:i], nums[i+1:]...)
// 			i--
// 		}
// 	}
// 	return len(nums)
// }

// two pointer solution
func removeDuplicates(nums []int) int {
	if len(nums) == 0 {
		return 0
	}

	k := 1 //pointer for unique elements

	for i := 1; i < len(nums); i++ {
		if nums[i] != nums[i-1] {
			nums[k] = nums[i]
			k++
		}
	}
	return k
}

// @lc code=end

