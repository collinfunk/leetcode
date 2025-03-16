/* Leetcode problem 2529: Maximum Count of Positive Integer and Negative Integer. */

package main

func maximumCount(nums []int) int {
	positive := 0
	negative := 0
	for i := 0; i < len(nums); i++ {
		if 0 < nums[i] {
			positive++
		} else if nums[i] < 0 {
			negative++
		}
	}
	if positive < negative {
		return negative
	}
	return positive
}
