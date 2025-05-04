/* Leetcode problem 1007: Minimum Domino Rotations For Equal Row. */

package main

func minDominoRotations(tops []int, bottoms []int) int {
	for _, target := range []int{tops[0], bottoms[0]} {
		missing_top := 0
		missing_bottom := 0
		for i := 0; i < len(tops); i++ {
			if target != tops[i] && target != bottoms[i] {
				break
			}
			if tops[i] != target {
				missing_top++
			}
			if bottoms[i] != target {
				missing_bottom++
			}
			if i == len(tops)-1 {
				return min(missing_top, missing_bottom)
			}
		}
	}
	return -1
}
