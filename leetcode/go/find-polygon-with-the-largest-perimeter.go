/* Leetcode problem 2971: Find Polygon With the Largest Perimeter. */

package main

import "sort"

func largestPerimeter(nums []int) int64 {
	sort.Ints(nums)
	side_sum := 0
	result := int64(-1)
	for _, value := range nums {
		if value < side_sum {
			result = int64(value + side_sum)
		}
		side_sum += value
	}
	return result
}

func main() {
}
