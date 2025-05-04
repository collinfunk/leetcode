/* Leetcode problem 781: Rabbits in Forest. */

package main

func numRabbits(answers []int) int {
	result := 0
	var table [1000]int
	for _, answer := range answers {
		if table[answer]%(answer+1) == 0 {
			result += answer + 1
		}
		table[answer]++
	}
	return result
}
