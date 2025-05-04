/* Leetcode problem 914: X of a Kind in a Deck of Cards. */

package main

func gcd(a, b int) int {
	for a != b {
		if a > b {
			a -= b
		} else {
			b -= a
		}
	}
	return a
}

func hasGroupsSizeX(deck []int) bool {
	var table [10000]int
	for _, card := range deck {
		table[card]++
	}
	divisor := -1
	for i := 0; i < 10000; i++ {
		if table[i] > 0 {
			if divisor <= 0 {
				divisor = table[i]
			} else {
				divisor = gcd(divisor, table[i])
			}
		}
	}
	return divisor >= 2
}
