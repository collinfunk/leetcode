/* Leetcode problem 3423: Maximum Difference Between Adjacent Elements in a Circular Array. */

package main

func abs(value int) int {
	if 0 < value {
		return value
	}
	return -value
}

func maxAdjacentDistance(nums []int) int {
	result := abs(nums[0] - nums[len(nums)-1])
	for i := 0; i < len(nums)-1; i++ {
		result = max(result, abs(nums[i]-nums[i+1]))
	}
	return result
}
