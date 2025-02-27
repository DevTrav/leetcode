/*
 * @lc app=leetcode id=1 lang=golang
 *
 * [1] Two Sum
 */

// @lc code=start

package main

// using hashmap
func twoSum(nums []int, target int) []int {
	numMap := make(map[int]int) //value -> index

	for i, num := range nums {
		complement := target - num
		if j, exists := numMap[complement]; exists {
			return []int{j, i}
		}
		numMap[num] = i
	}
	return []int{}
}

// @lc code=end
