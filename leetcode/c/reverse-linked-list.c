/* Leetcode problem 206: Reverse Linked List.  */

#include <stddef.h>

struct ListNode
{
  int val;
  struct ListNode *next;
};


struct ListNode *
reverseList (struct ListNode* head)
{
  struct ListNode *node = head;
  struct ListNode *prev = NULL;

  while (node)
    {
      struct ListNode *next = node->next;
      node->next = prev;
      prev = node;
      node = next;
    }

  return prev;
}
