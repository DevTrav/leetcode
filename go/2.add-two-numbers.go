/*
 * @lc app=leetcode id=2 lang=golang
 *
 * [2] Add Two Numbers
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	//create two pointers for l1 and l2
	//initialize the sum to zero
	//initialize the carry to zero

	l1Ptr := l1
	l2Ptr := l2

	dummyHead := &ListNode{}

	output := dummyHead
	carry := 0

	//loop through the lists as long as there is a node in either list or carry is not zero
	for l1Ptr != nil || l2Ptr != nil {
		sum := carry
		//add the values of the current nodes along with the carry
		if l1Ptr != nil {
			sum += l1Ptr.Val
			l1Ptr = l1Ptr.Next
		}
		if l2Ptr != nil {
			sum += l2Ptr.Val
			l2Ptr = l2Ptr.Next
		}
		carry = sum / 10
		digit := sum % 10

		output.Next = &ListNode{Val: digit}
		output = output.Next

	}
	if carry > 0 {
		output.Next = &ListNode{Val: carry}
	}
	return dummyHead.Next
}

// @lc code=end

