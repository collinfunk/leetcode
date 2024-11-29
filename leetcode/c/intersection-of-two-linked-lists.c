/* Leetcode problem 160: Intersection of Two Linked Lists.  */

#include <stddef.h>

struct ListNode
{
  int val;
  struct ListNode *next;
};


struct ListNode *
getIntersectionNode (struct ListNode *headA, struct ListNode *headB)
{
  if (headA == NULL || headB == NULL)
    return NULL;

  struct ListNode *nodeA = headA;
  struct ListNode *nodeB = headB;

  while (nodeA != nodeB)
    {
      nodeA = nodeA == NULL ? headB : nodeA->next;
      nodeB = nodeB == NULL ? headA : nodeB->next;
    }

  return nodeA;
}
