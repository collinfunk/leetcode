/* Leetcode problem 203: Remove Linked List Elements. */

#include <stdlib.h>

struct ListNode
{
  int val;
  struct ListNode *next;
};

struct ListNode *
removeElements (struct ListNode *head, int val)
{
  while (head != NULL && head->val == val)
    head = head->next;

  struct ListNode *node = head;

  while (node != NULL)
    {
      struct ListNode *next = node->next;
      if (next != NULL && next->val == val)
        node->next = next->next;
      else
        node = node->next;
    }

  return head;
}

int
main (void)
{
  return 0;
}
