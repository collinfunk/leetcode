/* Leetcode problem 876. Middle of the Linked List. */

package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func middleNode(head *ListNode) *ListNode {
	count := 0
	node := head
	for node != nil {
		node = node.Next
		count++
	}
	count /= 2
	node = head
	for count != 0 {
		count--
		node = node.Next
	}
	return node
}

func main() {
}
