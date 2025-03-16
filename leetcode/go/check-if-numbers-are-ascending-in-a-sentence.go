/* Leetcode problem 2042: Check if Numbers Are Ascending in a Sentence. */

package main

func areNumbersAscending(s string) bool {
	last := 0
	for i := 0; i < len(s); i++ {
		if s[i] >= '0' && s[i] <= '9' {
			current := int(s[i]) - int('0')
			if i+1 < len(s) && s[i+1] >= '0' && s[i+1] <= '9' {
				i++
				current *= 10
				current += int(s[i]) - int('0')
			}
			if current <= last {
				return false
			}
			last = current
		}
	}
	return true
}
