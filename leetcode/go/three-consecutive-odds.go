/* Leetcode problem 1550: Three Consecutive Odds. */

package main

func threeConsecutiveOdds(arr []int) bool {
	count := 0
	for _, num := range arr {
		if num&1 == 0 {
			count = 0
		} else {
			count++
			if count == 3 {
				return true
			}
		}
	}
	return false
}
