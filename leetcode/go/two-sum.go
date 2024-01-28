/* Leetcode problem 1: Two Sum. */

package main

func twoSum(nums []int, target int) []int {
	table := make(map[int]int)
	for index, value := range nums {
		need := target - value
		if need, ok := table[need]; ok {
			return []int{need, index}
		}
		table[value] = index
	}
	return nil
}

func main() {
}
