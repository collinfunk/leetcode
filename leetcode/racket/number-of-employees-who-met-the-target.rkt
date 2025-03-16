
;; Leetcode problem 2798: Number of Employees Who Met the Target.

(define/contract (number-of-employees-who-met-target hours target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (count (lambda (x) (>= x target)) hours))
