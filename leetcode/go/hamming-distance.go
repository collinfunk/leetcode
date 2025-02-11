/* Leetcode problem 461: Hamming Distance. */

package main

func hammingDistance(x int, y int) int {
	result := 0
	for 0 < x || 0 < y {
		if x&1 != y&1 {
			result++
		}
		x >>= 1
		y >>= 1
	}
	return result
}
