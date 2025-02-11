/* Leetcode problem 771: Jewels and Stones. */

package main

func numJewelsInStones(jewels string, stones string) int {
	table := make(map[byte]bool)
	result := 0
	for i := 0; i < len(jewels); i++ {
		table[jewels[i]] = true
	}
	for i := 0; i < len(stones); i++ {
		if _, exists := table[stones[i]]; exists {
			result++
		}
	}
	return result
}
