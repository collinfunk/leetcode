/* Leetcode problem 2553: Separate the Digits in an Array. */

package main

func separateDigits(nums []int) []int {
	var result []int
	temp := make([]int, 6)
	for _, value := range nums {
		i := 0
		for 0 < value {
			temp[i] = value % 10
			value /= 10
			i++
		}
		for 0 < i {
			i--
			result = append(result, temp[i])
		}
	}
	return result
}
