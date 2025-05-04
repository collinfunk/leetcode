/* Leetcode problem 3169: Count Days Without Meetings. */

package main

import "sort"

func countDays(days int, meetings [][]int) int {
	sort.Slice(meetings, func(i, j int) bool { return meetings[i][0] < meetings[j][0] })
	current := 1
	total := 0
	for _, m := range meetings {
		total += max(0, m[0]-current)
		current = max(current, m[1]+1)
	}
	return total + max(days-current+1, 0)
}
