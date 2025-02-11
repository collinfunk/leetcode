/* Leetcode problem 1114: Print in Order. */

#include <stdlib.h>
#include <pthread.h>
#include <stdio.h>

typedef struct
{
  pthread_mutex_t lock;
  pthread_cond_t cond;
  int turn;
} Foo;

void printFirst (void);
void printSecond (void);
void printThird (void);

Foo *
fooCreate (void)
{
  Foo *obj = malloc (sizeof *obj);
  if (obj == NULL)
    abort ();
  pthread_mutexattr_t attr;
  if (pthread_mutexattr_init (&attr) != 0
      || pthread_mutexattr_settype (&attr, PTHREAD_MUTEX_RECURSIVE) != 0
      || pthread_mutex_init (&obj->lock, &attr) != 0
      || pthread_mutexattr_destroy (&attr) != 0
      || pthread_cond_init (&obj->cond, NULL) != 0)
    abort ();
  obj->turn = 1;
  return obj;
}

void
first (Foo *obj)
{
  pthread_mutex_lock (&obj->lock);
  while (obj->turn != 1)
    if (pthread_cond_wait (&obj->cond, &obj->lock) != 0)
      abort ();
  printFirst ();
  obj->turn = 2;
  pthread_mutex_unlock (&obj->lock);
  pthread_cond_broadcast (&obj->cond);
}

void
second (Foo *obj)
{
  pthread_mutex_lock (&obj->lock);
  while (obj->turn != 2)
    if (pthread_cond_wait (&obj->cond, &obj->lock) != 0)
      abort ();
  printSecond ();
  obj->turn = 3;
  pthread_mutex_unlock (&obj->lock);
  pthread_cond_broadcast (&obj->cond);
}

void
third (Foo *obj)
{
  pthread_mutex_lock (&obj->lock);
  while (obj->turn != 3)
    if (pthread_cond_wait (&obj->cond, &obj->lock) != 0)
      abort ();
  printThird ();
  obj->turn = 1;
  pthread_mutex_unlock (&obj->lock);
  pthread_cond_broadcast (&obj->cond);
}

void
fooFree (Foo *obj)
{
  if (pthread_mutex_destroy (&obj->lock) != 0)
    abort ();
  free (obj);
}
